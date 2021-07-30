import random
start = input('請決定數字開始值: ')
end = input('請決定數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count +1
    number = input('請猜數字: ')
    number = int(number)
    if number == r:       
        print('終於猜對了!')
        print('你總共猜了', count, '次')
        break # 終止迴圈        
    elif number > r:
        print('比答案大!')
    elif number < r:
        print('比答案小!')
    print('這是你猜的第', count, '次') # 寫在if架構外，是為了避免重複同一行程式碼太多次