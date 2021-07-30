# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
r = random.randint(1, 100)
while True:
    number = input('請猜數字: ')
    number = int(number)
    if number == r:       
        print('終於猜對了!')
        break # 終止迴圈
    elif number > r:
        print('比答案大!')
    elif number < r:
        print('比答案小!')
    
           