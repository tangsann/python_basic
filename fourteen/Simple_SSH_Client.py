#!/usr/bin/python3
# -*- coding=utf-8 -*-
import paramiko
def simple_ssh_client(ip,username,password,command):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    x = stdout.read().decode()
    print(x)
    ssh.close()
if __name__ == '__main__':
    from argparse import ArgumentParser
    # simple_ssh_client('192.168.5.158','root','bjwlb@@555','ls')
    usage = "usage: python Simple_SSH_Client.py -i ipaddr -u username -p password -c command"
    parser = ArgumentParser(usage=usage)
    parser.add_argument("-i","--ipaddr",dest="ip",help="SSH Server",type=str)
    parser.add_argument("-u","--username",dest="username",help="SSH Username",default="root",type=str)
    parser.add_argument("-p","--password",dest="password",help="SSH Password",default="bjwlb@@555",type=str)
    parser.add_argument("-c","--command",dest="command",help="Shell Command",default="ls",type=str)
    args = parser.parse_args()
    simple_ssh_client(args.ip,args.username,args.password,args.command)



