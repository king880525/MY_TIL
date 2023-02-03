# MTD
## MTD란
- memory technology device의 약자
- char. device, block device와 같은 별도의 디바이스 
- FTL: Flash devcie 를 block device처럼 보이도록 변환해주는 Layer
- 기존의 block device용으로 개발된 파일 시스템을 flash memroy 위에서 사용 가능. 
- FTL 구현에 따라 성능이나 flash device의 수명이 큰 영향을 받게 된다.
- Wear Leveling: flash sector가 균등하게 사용되도록 FTL을 구현
- MTD는 FTL이 해당 Device를 control 할 수 있도록 도와주는 Low Level Driver
- device별로 device를 제어하는 방법이 다르기 때문에 MTD Layer에서 이를 일반화
- FTL은 하위 device의 제조사나 특정 제품에 상관 없이 구현 가능
- flash device를 위해 개발된 파일 시스템에서는 FTL 없이 file system이 MTD Layer 위에 올라가기도 한다.
- flash file system이 FTL을 포함하고 있는 경우도 있다.
## 유의점
- flash를 읽을 때는 상관없지만, 쓸 때는 한 block을 다 지우고 써야 한다.
- mtd->oobblock과 같이 mtd 구조체 변수로 받는 값을 통해서 최소 쓰기 크기를 확인할 수 있다.
## example code
``` c
#include <linux/mtd/mtd.h>

#define DVFLAG_MTDNAME "0:DVFLAG"
static struct dv_mtd_flash_info
{
    struct mtd_info * mtd;
    struct erase_info ei;
};

static struct dv_mtd_flash_info dv_mtd;
static int dv_flash_open(void)
{
    dv_mtd.mtd = get_mtd_device_nm(DVFLAG_MTDNAME);

    memset(&dv_mtd.ei, 0x00, sizeof(struct erase_info));
    dv_mtd.ei.mtd  = dv_mtd.mtd;
    dv_mtd.ei.addr = 0;
    dv_mtd.ei.len  = dv_mtd.mtd->erasesize;

    return 0;
}
static int dv_flash_read(void)
{
    int retlen = 0;
    char retbuf[128];

    dv_flash_open();

    memset(retbuf, 0x00, sizeof(retbuf));
    if(!mtd_read(dv_mtd.mtd, 0, 15, &retlen, retbuf)) {
        printk(KERN_DEBUG "DAVO|JIH|0|%30s()[%04d] : -----------------------------------retbuf: %s, retlen: %d\n", __FUNCTION__, __LINE__, retbuf, retlen);
    }   
    return 0;
}

static int dv_flash_write(void)
{
    int retlen = 0;
    char buf[128];
    char retbuf[2048];

    dv_flash_open();

    memset(retbuf, 0xff, sizeof(retbuf));
    snprintf(retbuf, sizeof(retbuf), "%s", dvsock_msg);

    mtd_erase(dv_mtd.mtd, &dv_mtd.ei);
    if(!mtd_write(dv_mtd.mtd, 0, sizeof(retbuf), &retlen, retbuf)) {
        printk(KERN_DEBUG "DAVO|JIH|0|%30s()[%04d] : -----------------------------------retbuf: %x%x, retlen: %d\n", __FUNCTION__, __LINE__, retbuf[0], retbuf[1], retlen);
    } else {
        printk(KERN_DEBUG "DAVO|JIH|0|%30s()[%04d] : ----------------------------------- write error\n", __FUNCTION__, __LINE__);
    }
    return 0;
}
```
### 출처
http://dooeui.blogspot.com/2009/01/mtd.html
https://fmyson.tistory.com/337
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sparcman1&logNo=10093814136