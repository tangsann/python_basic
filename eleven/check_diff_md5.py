#!/usr/bin/python3
# -*- coding=utf-8 -*-
from python_basic.nine.paramiko练习_ssh import get_ssh
import re
import hashlib
import time

def get_config(ip, username='admin', password='123456'):
    try:
        device_config_raw = get_ssh(ip, username, password, cmd='show running-config')
        split_result = re.split(r'\r\nhostname \S+\r\n',device_config_raw)
        device_config = device_config_raw.replace(split_result[0],'').strip()
        return device_config
    except Exception:
        return
def check_diff(ip, username='admin', password='123456'):
    beforce_md5 = ''
    try:
        while True:
            device_config = get_config(ip, username, password)
            m = hashlib.md5()
            m.update(device_config.encode())
            md5_value = m.hexdigest()
            print(md5_value)
            if not beforce_md5:
                beforce_md5 = md5_value
            elif beforce_md5 != md5_value:
                print('MD5 value changed')
                break
            time.sleep(5)
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    # print(qytang_get_config('192.168.3.200', username='admin', password='123456'))
    check_diff('192.168.3.200', username='admin', password='123456')
