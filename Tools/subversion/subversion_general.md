# svn 카피
svn 카피
``` bash
$ svn copy svn://SERVER/PROJECT/trunk svn://SERVER/PROJECT/branches/0.6.1
```
# svn 머지
``` bash
$ svn merge file:///home/heyduk/repos/project1/trunk file:///home/heyduk/repos/project2/trunk my_work
```
저장소의 project1과 project2간의 차이를 지역 작업본인 my_work에 병합함
``` bash
$ svn merge -r 6:7 file;///home/heyduk/repos/trunk my_work
```
저장소의 리비전 6~7의 변경내용을 지역 작업본인 my_work 에 병합함 
``` bash
$ svn merge -r 1318:1339 svn://172.17.122.9/mtk-openwrt-lede-4.2.1.0/trunk ntv4ov6
```
특정 리비전 merge