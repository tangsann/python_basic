#!/usr/bin/python3
# coding=utf-8
import re
from nine import paramiko练习
def ssh_get_route(ip,username,password,cli='route -n'):
    route_result = paramiko练习.get_ssh(ip,username,password,cmd=cli)
    ipv4_gw = re.match(r'^Kernel[\s\S]+0.0.0.0\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+0.0.0.0\s+UG[\s\S]+$', route_result).groups()[0]
    return ipv4_gw
if __name__ == '__main__':
    print('网关为：')
    print(ssh_get_route('192.168.5.158','root','bjwlb@@555'))
