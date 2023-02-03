## strsep - 문자열을 delimiter 단위로 분리
``` C
#include <string.h>

char *strsep(char **stringp, const char *delim);
```
ex)
``` C
#include <string.h>

char *strsep(char **stringp, const char *delim)
{
    char *ptr = *stringp;

    if(ptr == NULL) {
        return NULL;
    }

    while(**stringp) {
        if(strchr(delim, **stringp) != NULL) {
            **stringp = 0x00;
            (*stringp)++;
            return ptr;
        }
        (*stringp)++;
    }
    *stringp = NULL;

    return ptr;
}
```
참조) https://www.it-note.kr/87 [IT 개발자 Note:티스토리]

strtok
strtok_r
strsep
https://uple.net/2535
https://kldp.org/node/21895
https://jybaek.tistory.com/593
https://kldp.org/node/38574
https://hahaite.tistory.com/306