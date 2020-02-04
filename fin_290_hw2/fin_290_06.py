import random

# 题目出的太宽了，我限制了下就猜100内整数

zzh = random.randint(1,100)

guess_num = 0
attempts = 5 # 总共5次尝试机会

print(f'Please guess the number in 1-100 interval~~')

# 这里相当于是个死循环，不断的尝试，限制次数使用完成
while int(guess_num) !=zzh and attempts !=0:

    print(f'hey bro,input guess number: ')
    print(f'Now u have {attempts} chances to try')
    guess_num = input()

    if not guess_num.isdigit(): # 判断输入的字符串是否为数字
        print(f'Please input a number,not any other type of things: ')
        guess_num = 0
        attempts -= 1
        continue # 终止本次循环，进入下一次循环验证
    else:
        if int(guess_num) > zzh:
            print('oops,Bigger yo~~')
        elif int(guess_num) < zzh:
            print('oops,Smaller yo~~')
    attempts -= 1

if int(guess_num) == zzh:
    print(f'Bingo!!!!!!!!!!!!!!!!NiuBlity')
else:
    print(f'GoodBye.No chances')
    print(f'The number is :{zzh}' )
