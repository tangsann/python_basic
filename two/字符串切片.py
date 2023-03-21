#!/usr/bin/python3
# coding=utf-8
word = " scallywag"
s = word.strip()
i = s.find('ally')
j = s.find('wag')
sub_word = s[i:j]
print(sub_word)

