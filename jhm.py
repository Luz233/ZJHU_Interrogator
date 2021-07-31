#coding:utf-8
#激活码生成
#
import string
import random

quyu = string.digits +string.ascii_letters

def get_key(n):
    key = ''
    for i in range(1,n+1):
        key += random.choice(quyu) #获取随机字符或数字
        if i % 4 == 0 and i !=n: #每隔4个字符增加'-'
            key += '-'
    print(key)
    return key

def get_all_keys():
    tmp=[]
    for i in range(m):
        one_key = get_key(n)
        if one_key not in tmp: #去掉重复key
            tmp.append(one_key)
    for key in tmp:
        with open('3.txt','a+') as f:
            f.write(key+'\n') #写入激活码
            #f.write('\r\n')



m = int(input('输入要生成的激活码数量,输入0退出:'))
n = int(input('输入激活码长度'))
get_all_keys()