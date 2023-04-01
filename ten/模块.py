#!/usr/bin/python3
# -*- coding=utf-8 -*
from python_basic.eight.函数_ping import ping
from python_basic.nine.paramiko练习_ssh import get_ssh
# from paramiko练习_ssh import get_ssh
# from 函数_ping import ping
import re
import pprint
def qytang_get_if(*ips, username='admin', password='123456'):
    device_if_dict = {}
    for ip in ips:
        if_dict = {}
        if ping(ip):
            for line in get_ssh(ip, username, password, cmd='show ip interface brief').split('\n'):
                # print(line)
                re_result = re.match(r'([A-Z]\S+\d+)\s+'
                                     r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                                     r'\w+\s+\w+\s+\w+\s+\w+',line.strip())
                if re_result:
                    if_dict[re_result.groups()[0]] = re_result.groups()[1]
        device_if_dict[ip] = if_dict

    return device_if_dict
if __name__ == "__main__":
    pprint.pprint(qytang_get_if('192.168.3.100', '192.168.3.101', username='admin', password='123456'), indent=4)
