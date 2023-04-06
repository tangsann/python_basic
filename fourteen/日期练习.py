#!/usr/bin/python3
# -*- coding=utf-8 -*-
from datetime import datetime,timedelta
five_days_ago = datetime.now() - timedelta(days=5)
five_days_ago_str_1 = five_days_ago.strftime('%Y-%m-%d_%H-%M-%S')
five_days_ago_str_2 = str(five_days_ago)
filename = 'save_fivedaysago_time_'+five_days_ago_str_1
wf = open(filename+'.txt','w')
wf.write(five_days_ago_str_2)
wf.close()
