# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:21:05 2021

@author: Win10
"""

driving = input('請問你有沒有開過車 ?  ')
if driving != '有' and driving != '沒有':
    print('只能輸入有或沒有')
    raise SystemExit

age = int(input('請問你的年齡 : '))
if driving == '有':
    if age >= 18:
        print('你通過測驗')
    else:
        print('奇怪, 你怎會開過車')
else:
    if age >= 18:
        print('你可以考駕照了!! 怎麼還不去考')
    else:
        print('很好, 再過幾年就可以考駕照了')
