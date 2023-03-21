#!/usr/bin/python3
# coding=utf-8
import re
str1 = 'Port-channel1.189    192.168.189.254  YES    CONFIG  up '
re_str1 = re.match('^([A-Z]\S+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+[A-Z]+\s+[A-Z]+\s+([a-z]+)\s+$',str1).groups()
interfaces = re_str1[0]
ip = re_str1[1]
status = re_str1[2]
print('-'*50)
print('%-8s : %s '%('接口',interfaces))
print('%-8s : %s '%('IP地址',ip))
print('%-8s : %s '%('状态',status))
