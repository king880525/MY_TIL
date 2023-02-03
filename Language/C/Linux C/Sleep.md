## sleep, delay, shcedule
1. CPU 소모성 API
지정한 지연시간까지 loop 를 돌면서 cpu 시간을 소모하는 형태의 API 입니다.
 ``` C
 #include <delay.h>
void ndelay(unsigned long nsec);
void udelay(unsigned long usec);
void mdelay(unsigned long msec);
```
•위의 함수들은 SW loop 를 사용한다.
•위의 함수로 최대로 delay 시킬수 있는 값은 제한되어있다. (__bad_udelay )
•실행대기 함수들로, 위의 함수들을 실행하는 동안에는 다른 TASK 를 실행하지 않는다. (contex switching 이 안 일어 나는 듯;;)
•delay 할 수 있는 시간의 단위만 다를 뿐 동작내용 상으로는 jitbusy 와 동일하다
2. CPU 소모가 없는 API
CPU 점유가 없이 시간 지연을 구현하려면 현재 자기자신한테 할당된 프로세스 시간을 반납하고 대기하는 방식을 사용하면 됩니다.
``` C
#include <linux/delay.h>
#include <linux/timer.h>
sleep();//초단위
msleep();//msec 1/1000초
usleep();//micro초 1/1000000초
msleep_interruptible();
schedule_timeout_interruptible();
schedule_timerout_uninterruptible();
schedule_timeout();
```
차이점
•msleep / ssleep : 호출한 프로세스가 잠든다. 잠든 동안에는 인터럽트가 불가능 하다.
•msleep_interruptible : msleep 과 동일하나 인터럽트가 가능함.

커널 소스상의 관계
•ssleep() 는 msleep() 를 호출합니다.
•msleep() 는 schedule_timeout_uninterrupt() 를 호출합니다.
•schedule_timeout_uninterrupt() 는 schedule_timeout() 을 호출합니다.