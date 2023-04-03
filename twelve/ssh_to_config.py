#!/usr/bin/python3
# -*- coding=utf-8 -*-
import re
import paramiko
from time import sleep


def get_client(ip,username,password,enable):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, port=22, username=username, password=password)
    cli = ssh.invoke_shell()
    cli.send('terminal length 0\n'.encode())
    cli.send(('enable\n' + enable + '\n').encode())
    return cli

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=3, verbose=False):
    chan =get_client(ip, username, password,enable)
    for cmd in cmd_list:
        chan.send('{}\n'.format(cmd).encode())
        sleep(wait_time)
        device_result = chan.recv(9999).decode()
        if verbose:
            print(device_result)

if __name__ == '__main__':
    cmd_list = ['show version','configure terminal','router ospf 1']
    qytang_multicmd('192.168.3.200', 'admin', '123456', cmd_list, enable='123456', wait_time=2, verbose=True)
