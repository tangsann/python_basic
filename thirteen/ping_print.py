#!/usr/bin/python3
# -*- coding=utf-8 -*-
from kamene.all import *
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
class Ping:
    def __init__(self,ip,srcip='192.168.3.75',length=100):
        self.ip = ip
        self.srcip = srcip
        self.length = length
    def one(self):
        data='a'*self.length
        ping_pkt = IP(dst=self.ip,src = self.srcip)/ICMP()/data
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        if ping_result:
            print(f'{self.ip} 可达！')
    def ping(self,online='!',timeout='.'):
        data = 'a' * self.length
        ping_pkt = IP(dst=self.ip, src=self.srcip)/ICMP()/data
        for count in range(5):
            ping_result = sr1(ping_pkt, timeout=2, verbose=False)
            if ping_result and count <4:
                print(online,end='')
            elif ping_result and count ==4:
                print(online)
            elif ping_result==None and count <4:
                print(timeout, end='')
            elif ping_result == None and count == 4:
                print(timeout)
    def __str__(self):
        if self.srcip == '192.168.3.75':
            return f'<{self.__class__.__name__}=> dstip:{self.ip}, size:{self.length}>'
        else:
            return f'<{self.__class__.__name__}=> srcip:{self.srcip}, dstip:{self.ip}, size:{self.length}>'
class NewPing(Ping):
    def ping(self):
        Ping.ping(self,online='+',timeout='?')
if __name__ == '__main__':
    ping = Ping('192.168.3.1')
    total_len = 70
    def print_new(word,s='-'):
        print('{}{}{}'.format(s * int((total_len-len(word))/2),word,s * int((total_len-len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload length')
    ping.length = 200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.srcip = '192.168.3.201'
    print(ping)
    ping.ping()
    print_new('new class NewPing',s='=')
    newping = NewPing('192.168.3.1')
    newping.length = 300
    print(newping)
    newping.ping()











