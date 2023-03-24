#!/usr/bin/python3
# coding=utf-8
import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
ipv4_add = re.findall('inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall('netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
broadcast = re.findall('broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
mac_addr = re.findall('ether\s+([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})',ifconfig_result)[0]
format_string = '{:}'
print(format_string.format('%-10s'%'ipv4_add' +':' + ipv4_add))
print(format_string.format('%-10s'%'netmask' +':' + netmask))
print(format_string.format('%-10s'%'broadcast' +':' + broadcast))
print(format_string.format('%-10s'%'mac_addr' +':' + mac_addr))
ipv4_gw = ipv4_add.replace(ipv4_add[-3:],'254')
print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为 :' + ipv4_gw + '\n')
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result = re.match('^PING[\s\S]+From[\s\S]+(icmp_seq=1\s+Destination\s+Host\s+Unreachable)[\s\S]+$',ping_result).groups()
if re_ping_result:
    print('网关不可达!')
else:
    print('网关可达!')