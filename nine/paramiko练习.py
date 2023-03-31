#!/usr/bin/python3
# coding=utf-8
import paramiko
def get_ssh(ip,username,password,port=22,cmd='ls test'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x
if __name__ == '__main__':
    print(get_ssh('192.168.5.158','root','bjwlb@@555'))
    print(get_ssh('192.168.5.158','root','bjwlb@@555',cmd='pwd'))
