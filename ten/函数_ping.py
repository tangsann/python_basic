#!/usr/bin/python3
# -*- coding=utf-8 -*-
from kamene.all import *
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 关闭不必要的报错
def ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
    if ping_result:
        return ip
if __name__=='__main__':
    ping_tong = ping('192.168.3.1')
    if ping_tong[1]:
        print(f'{ping_tong[0]}通！')
    else:
        print(f'{ping_tong[0]}不通！')

