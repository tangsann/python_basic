#!/usr/bin/python3
# coding=utf-8
import re
str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
new_str = re.split('\s',str)
vlan_id = new_str[0]
mac = new_str[1]
type = new_str[2]
interfaces = new_str[3]
print('%-12s :' % 'VLAN ID',vlan_id)
print('%-12s :' % 'MAC',mac)
print('%-12s :' % 'Type',type)
print('%-12s :' % 'Interfaces',interfaces)

