#!/usr/bin/python3
# coding=utf-8
import re
str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
str = re.sub(',','',str)
str_new = str.split()
print('%-12s :%-12s' % ('protoclo',str_new[0]))
print('%-12s :%-12s' % (str_new[1],str_new[2]))
print('%-12s :%-12s' % (str_new[3],str_new[4]))
print(f'{str_new[5]:<12} :{str_new[6]:<12}')
print(f'{str_new[7]:<12} :{str_new[8]:<12}')
print(f'{str_new[9]:<12} :{str_new[10]:<12}')
