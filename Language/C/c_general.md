# 빌드
## 에러 메시지
`aggregate value used where an integer was expected`
=> c 구조체를 직접 integer로 캐스팅 하려 함.

ntohl 헤더
- netinet/in.h 헤더를 포함 해야한다.
- 
## Trouble Shooting
``` C
char temp[20];
char arr_idx = 0;

temp[arr_idx];
```
=> array subscript has type 'char' error
-> gcc에서 배열을 읽을 때 unsigned 형으로 하지 않을 때 발생하는 경고
-> 배열의 인덱스 값이 음수가 될 수 있으므로 이를 방지 하기 위해 에러 출력

## 프로그램 처리 시간 구하기
``` C
#include <stdio.h>
#include <time.h>

int main(void)
{
	int start_time, end_time;

	start_time = clock();
	routine();
	end_time = clock();
	printf("process time: %d", (end_time - start_time)/CLOCKS_PER_SEC);
	
	return 0;
}
```
=> routine 실행 동안의 clock의 차이를 구할 수 있다.
=> clock의 차이를 CLOCKS_PER_SEC로 나눠주면, routine 실행 시간 동안의 처리 시간을 초단위로 구할 수 있다.
