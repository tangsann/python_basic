#!/usr/bin/python3
# coding=utf-8
import re
str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
str = re.sub(',','',str)
str_new = re.split('\s',str)
time = re.split(':',str_new[6])
print('%-12s :%-12s' % ('protoclo',str_new[0]))
print('%-12s :%-12s' % (str_new[1],str_new[2]))
print('%-12s :%-12s' % (str_new[3],str_new[4]))
print(f'{str_new[5]:<12} :{time[0]:<2}小时{time[1]:>3}分钟{time[2]:>3}秒')
print(f'{str_new[7]:<12} :{str_new[8]:<12}')
print(f'{str_new[9]:<12} :{str_new[10]:<12}')
