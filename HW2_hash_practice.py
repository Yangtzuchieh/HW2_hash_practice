# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:07:18 2023

@author: David
"""
#建一個dict
my_dict = {}
#紀錄不同字個數，預設為0
word_count = 0
#讀檔案
inputfile = open('hw2_data.txt','r')
line = inputfile.readline()
line = line.rstrip()
while line != '':
    #將沒有出現在dict裡面的key預設為0
    my_dict.setdefault(line, 0)
    #如果key為0代表這個字還沒有出現，key設為1
    if my_dict[line] == False:
        my_dict[line] = 1
        word_count += 1
    #已經在dict裡面的字key直接加1
    else:
        my_dict[line] += 1   
    #換讀下一行
    line = inputfile.readline()
    line = line.rstrip()
#輸出結果
print('總共有', word_count, '個不重複的英文字')
print('每一個英文字出現次數:')
for i in my_dict:
    print(i, my_dict[i])