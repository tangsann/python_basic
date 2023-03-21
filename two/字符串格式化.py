#!/usr/bin/python3
# coding=utf-8
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURESE_FEES_SEC = 456789.12456
COURESE_FEES_Python = 1234.3456
#字符串格式化表达式（传统方法）
#line1 ='Department1 name:%-12sManager:%-12sCOURSE FEES:%-12.2fThe End!' % (department1,depart1_m,COURESE_FEES_SEC)
#line2 ='Department2 name:%-12sManager:%-12sCOURSE FEES:%-12.2fThe End!' % (department2,depart2_m,COURESE_FEES_Python)
#字符串格式化方法（新方法）
#line1 = 'Department1 name:{:<12}Manager:{:<12}COURSE FEES:{:<12.2f}The End!'.format(department1,depart1_m,COURESE_FEES_SEC)
#line2 = 'Department2 name:{:<12}Manager:{:<12}COURSE FEES:{:<12.2f}The End!'.format(department2,depart2_m,COURESE_FEES_Python)
#f-string
line1 = f'Department1 name:{department1:<12}Manager:{depart1_m:<12}COURSE FEES:{COURESE_FEES_SEC:<12.2f}The End!'
line2 = f'Department1 name:{department2:<12}Manager:{depart2_m:<12}COURSE FEES:{COURESE_FEES_Python:<12.2f}The End!'
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
