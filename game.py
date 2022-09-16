""" 用Python设计第一个游戏 """

while True:
    temp = input('猜一下数字')
    guess = int(temp) # 如果temp不是数字或不能被转换为数字，则会报错

    if guess == 8:
        print("对了")
        print("没奖励")
        break
    else:
        if guess < 8:
            print('小了')
        else:
            print('大了')

print("结束")
