import random
r = random.randint(1, 100)
count = 0
while True:
    count = count + 1
    num = input('請猜數字： ')
    num = int(num)
    if num == r:
        print('恭喜你猜中了! ')
        break
    elif num > r:
    	print('比答案大', '這是你猜的第', count, '次')
    elif num < r:
    	print('比答案小', '這是你猜的第', count, '次')


