#!/usr/bin/python3
# coding=utf-8
word = input("请输入原始单词为:\n")
new_word = word[1:] + '-' + word[0] + 'y'
print('转换后的单词为:\n' + new_word)
