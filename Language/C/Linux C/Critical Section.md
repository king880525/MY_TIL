# Critical Section
공유되는 자원에 동시에 접근이 발생하여 문제가 발생하지 않도록 독점성을 보장해주는 영역.
# Spinlock
- Signaling mechanism. 
- 현재 공유자원에 접근할 수 있는 쓰레드, 프로세스의 수를 나타내는 값을 두어 상호배제를 달성하는 기법
- busy-waiting: lock을 획득하기 전까지 특정 루프를 돌면서 대기
- spinlock 동작에 문제가 생기면 Watchdog Reset으로 시스템 리셋
## spin_lock
### 구현
- 실제 구현부는 __raw_spin_lock() 함수
- spin_lock -> raw_spin_lock -> __raw_spin_lock
- preempt_count_add(1) 함수 호출로 irq 호출될 시 preemption 차단
- do_raw_spin_lock() 함수를 호출
### 사용
- spinlock을 거는 구간이 빨리 수행되거나 IRQ가 trigger되어 preemption되어도 문제가 안될 때 사용
- spin_lock 내 함수 호출이 없는 경우 사용.
## spin_lock_irq
### 구현
- 실제 구현부는 __raw_spin_lock_irq() 함수
- spin_lock_irq -> raw_spin_lock_irq -> __raw_spin_lock_irq
- arch_local_irq_disable()을 호출해버려서
-  "msr daifset, #2" ARM64(Aarch64) 인스트럭션이 수행 - > IRQ가 하드웨어적으로 Trigger가 안되게 차단.
- preempt_count_add(1)을 호출 -> IRQ trigger 시 preemption이 안 되도록 방지
- arch_local_irq_disable()을 호출해버려서 "msr daifset, #2" ARM64(Aarch64) 인스트럭션이 수행
- spin_unlock_irq()이 수행될 때 까지 아예 IRQ가 하드웨어적으로 Trigger 안 됨.
### 사용
- spin_lock_irq()는 거는 구간이 너무 오래 수행되는 코드면 시스템이 느려진다.
## spin_lock_irqsave
### 구현
- 실제 구현부는 __raw_spin_lock_irqsave() 함수
- raw_spin_lock_irqsave -> _raw_spin_lock_irqsave -> __raw_spin_lock_irqsave
- arch_local_irq_save()함수
- [1]: "mrs %0, daif" // Interrupt disable flag을 설정한 후 해당 값을 flags에 저장
- [2]:"msr daifset, #2"" // 하드웨어적으로 IRQ를 disable함
- spin_unlock_irqrestore() 함수가 호출 시 아래 순서로 arch_local_irq_restore() 함수의 파라미터로 사용
 - __raw_spin_unlock_irqrestore -> local_irq_restore -> arch_local_irq_restore
- interrupt flags를 가져오는 것 외에 spin_lock_irq() 함수랑 기능적으로 다른게 없다.
## 출처
https://worthpreading.tistory.com/90
http://rousalome.egloos.com/9966342
http://rousalome.egloos.com/9967067

# Mutex
- 뮤텍스는 휴면을 지원하며 프로세스 컨택스트에서 주로 쓰는 락(Locking) 기법
- 한 쓰레드, 프로세스에 의해 소유될 수 있는 Key🔑를 기반으로 한 상호배제기법
- mutex lock에 문제가 생기면 보통 키보드 동작이 안되거나 모바일인 경우 터치 동작이 안되듯 락업으로 문제가 재현
## 뮤텍스 획득   
- 이미 뮤텍스를 다른 프로세스가 획득했으면 휴면에 진입
- mutex lock이 lock을 획득하지 못하면 struct mutex.wait_list에 등록하고 sleep
## 뮤텍스 해제
- 뮤텍스를 기다리며 휴면에 진입한 프로세스를 깨움
## struct mutex
``` C
struct mutex {
    atomic_long_t		owner;
    spinlock_t		wait_lock;
#ifdef CONFIG_MUTEX_SPIN_ON_OWNER
    struct optimistic_spin_queue osq; /* Spinner MCS lock */
#endif
    struct list_head	wait_list;
#ifdef CONFIG_DEBUG_MUTEXES
    void			*magic;
#endif
#ifdef CONFIG_DEBUG_LOCK_ALLOC
    struct lockdep_map	dep_map;
#endif
};
```
atomic_long_t owner;
- 뮤텍스를 획득한 프로세스의 태스크 디스크립터 주소를 저장

struct list_head wait_list;
- 뮤텍스락을 기다리는 프로세스 정보
## struct mutex_waiter
``` c
struct mutex_waiter {
	struct list_head	list;
	struct task_struct	*task;
	struct ww_acquire_ctx	*ww_ctx;
#ifdef CONFIG_DEBUG_MUTEXES
	void			*magic;
#endif
};
```
struct list_head	list;
- 뮤텍스를 획득을 시도하가 잠든 프로세스의 연결 리스트 
- struct mutex 구조체 wait_list 필드가 list 필드 주소를 저장
  
struct task_struct	*task;
- 뮤텍스를 기다리는 프로세스의 태스크 디스크립터 주소
- 뮤텍스를 어느 프로세스가 획득했는지 알 수 있는 핵심 자료구조입니다.
## 뮤텍스에서 fastpath와 slowpath
- 뮤텍스 실행 흐름은 fastpath와 slowpath 루틴으로 분류
- fastpath;
  - 뮤텍스는 다른 프로세스가 이미 획득하지 않은 상태면 바로 획득 가능.
  - fastpath 로 빨리 뮤텍스를 획득하고 해제합니다.
- slowpath;
  - 다른 프로세스가 이미 뮤텍스를 획득한 경우 실행하는 동작입니다. 
  - 1. 뮤텍스를 획득을 하지 못한 프로세스는 대기열에 자신을 등록하고 휴면
  - 2. 뮤텍스를 해제한 프로세스는 뮤텍스 대기열에 등록(뮤텍스 획득을 이미 시도)한 다른 프로세스를 깨움
## Fast Path
- fastpath는 뮤텍스를 다른 프로세스가 획득하지 않았을 때 뮤텍스를 획득하고 빠져 나오는 실행 흐름
- 뮤텍스를 획득하려면 mutex_lock() 함수를 호출
- mutex_lock() 함수 내부 루틴에서 다음 순서로 동작
  - struct mutex 구조체 owner 필드 점검 
- owner가 0x0이니 뮤텍스를 다른 프로세스가 획득하지 않은 상태로 판단
- owner: 뮤텍스를 획득한 프로세스의 태스크 디스크립터를 저장
## Slow Path
- 뮤텍스는 프로세스 뮤텍스를 획득할 때 조건에 따라 fastpath와 slowpath로 실행 흐름를 분류할 수 있습니다.
- fastpath: 뮤텍스를 획득한 적이 없어서 뮤텍스 획득 
- slowpath: 뮤텍스를 이미 획득해 휴면에 진입한 후 깨어남
mutex_lock()
__mutex_lock_slowpath()
__mutex_lock() 
__mutex_lock_common

## 출처
http://rousalome.egloos.com/10003460

# Semaphore
## 사용 목적
- spinlock은 선점을 비활성화하고, 필요에 따라서 interrupt나 bottom half도 비활성화
- spinlock이 오랫동안 락을 들고있으면 오랫동안 스케줄링과 인터럽트가 처리되지 않는 문제 발생
- spinlock은 그 특성상 락을 획득한 동안에는 sleep이 불가능
- 락을 하는 시간이 길면, spinlock 대신, "sleeping lock"인 semaphore를 사용
## down_interruptable
- 임계영역(critical section)에 대한 제어권을 얻기 위해 호출
- 이미[[2022-08-08]]다.
- wait 상태에서 interrupt에 의해서 깨어날 수 있다. (소프트웨어 인터럽트, Signal)
- Signal에 의해서 깨어난 경우, EINTR을 반환한다.
## down
- down_interruptable와 비슷하지만 interrupt에 의해 깨어날 수 없다.
## down_trylock
- down/down_interruptable은 임계영역에 대한 제어권을 얻지 못 하면 sleep 상태가 된다.
- down_trylock은 제어권을 얻지 못 하면 0이 아닌 값을 반환한다.
## semaphore API
### 1. Header
``` c
<asm/semaphore.h>
```
혹은
``` c
#include <linux/semaphore.h>
```
### 2. 초기화
``` c
void sema_init(struct semaphore *sem, int val);
```
val: semaphore에 설정할 초기값

`mutex로 사용할 때, 정적 초기화`
``` c
DECLARE_MUTEX(name); // 1로 초기화.
DECLARE_MUTEX_LOCKED(name); // 0으로 초기화.
```
`mutex로 사용할 때, 실행 중 초기화`
``` c
void init_MUTEX(struct semaphore *sem); // 1로 초기화.
void init_MUTEX_LOCKED(struct semaphore *sem); // 0으로 초기화
```
### 3. 세마포어 획득
``` C
void down(struct semaphore *sem);
int down_interuptible(struct semaphore *sem);
int down_ttylock(struct semaphore *sem);
```
### 4. 세마포어 반환
``` C
void up(struct semaphore *sem);
```
## semaphore API - 읽기/쓰기
- 읽기만 수행하는 스레드라면 여러 스레드가 한 번에 접속 가능
- rwsem 이라는 특수 세마포어를 이용
- rwsem 을 사용하면 쓰기 스레드 하나 혹은 읽기 스레드 여럿이 세마포어를 할당 받도록 구현 
- 우선순위는 쓰기 스레드에게 있다. 
- 쓰기 스레드가 임계구역에 접근하면 읽기 스레드는 쓰기 스레드가 작업을 끝낼 때까지 기다려야 한다. 
- 쓰기 스레드가 많을 경우 읽기 스레드가 오랫동안 접근 권한을 얻지 못할 수 있다. 
- 쓰기 접근이 매우 드물고, 짧은 시간 동안에만 필요한 경우에 사용
### 1. 초기화
  ``` c
  void init_rwsem(struct rw_semaphore *sem);
  ```
### 2. 읽기 전용 세마포어 사용
``` c
void_down_read(struct rw_semaphore *sem);
int down_read_ttylock(struct rw_semaphore *sem);
```
### 3. 읽기 전용 세마포어 해제
``` c
void up_read(struct rw_semaphore *sem);
```
### 4. 쓰기 전용 세마포어 사용
``` c
void down_write(struct rw_semaphore *sem);
int down_write(struct rw_semaphore *sem);
```
### 5. 쓰기 전용 세마포어 해제
``` c
void up_write(struct rw_semaphore *sem);
```
잠시만 쓰기 락을 걸어 수정하고 한동안은 읽기 권한만 필요하다면
``` c
void downgrade_write(struct rw_semaphore *sem);
```
## 출처
https://decdream.tistory.com/296
https://blog.dasomoli.org/246/
https://hyeyoo.com/86
https://hyeyoo.com/87?category=900545
## 참조
https://blackinkgj.github.io/Semaphore/
https://jwprogramming.tistory.com/13