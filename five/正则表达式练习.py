#!/usr/bin/python3
# coding=utf-8
import os
import re
route_n_result = os.popen('route -n').read()
ipv4_gw = re.match('^Kernel[\s\S]+0.0.0.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0.0.0.0\s+UG[\s\S]+$',route_n_result).groups()
print('网关为:' + ipv4_gw[0])