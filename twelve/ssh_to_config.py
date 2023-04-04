#!/usr/bin/python3
# -*- coding=utf-8 -*-
import paramiko
from time import sleep

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=5, verbose=False):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, port=22, username=username, password=password)
    chan = ssh.invoke_shell()
    chan.send('terminal length 0\n'.encode())
    chan.send(('enable\n' + enable + '\n').encode())
    device_result = ''
    for cmd in cmd_list:
        chan.send('{}\n'.format(cmd).encode())
        sleep(wait_time)
        device_result = device_result + chan.recv(9999).decode()
    if verbose:
        return device_result

if __name__ == '__main__':
    cmd_list = ['show version','configure terminal','router ospf 1','network 192.168.4.0 0.0.0.255 area 0']
    print(qytang_multicmd('192.168.3.200', 'admin', '123456', cmd_list, enable='123456', wait_time=2, verbose=True))

