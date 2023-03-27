#!/usr/bin/python3
# coding=utf-8
l1 = [4,5,7,1,3,9,0]
l2 = l1.copy()
l2.sort()
#copy和sort，可以使用下面一条代码代替
#l2 = sorted(l1)
for i in range(len(l1)):
    print(l1[i],l2[i])

