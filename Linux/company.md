# 회사 업무 관련
`iwpriv rax3 DisConnectSta=b2:7e:fa:0e:10:5b`
`iwpriv rax0 set debug=0:12:0`
`while [ 1 ]; do sleep 1; apstats -d | grep ra; done`
`logread -l 10 -f | grep "TX Counter" -A 20 &`
dma
ring buffer