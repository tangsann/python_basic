#!/usr/bin/python3
# coding=utf-8
import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
print(ifconfig_result)

ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)
print(ipv4_add)
# netmask = re.findall()
# broadcast = re.findall()
# mac_addr = re.findall()
