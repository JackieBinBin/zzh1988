# write code that outputs the first N-terms of the Fibonacci sequence
# where N is input by a user
# EG:1, 1, 2, 3, 5, 8, 13, 21, . . .

user_input = int(input(f'Please input a number N: '))

# 核心即为每个数均为前两项之和
# 用户输入的数字即为数据项长度

# def zzh_fibo (n):
#     if n == 1 or n == 2:
#         return 1
#     return zzh_fibo (n-1) + zzh_fibo (n-2)
#
# fibo_list = []
#
# for i in range(1,user_input):
#     fibo_list.append(zzh_fibo(i))

# print(f'fibo 序列结果：{fibo_list}')

# 思路同上，N作为列表下标在不断的循环，
#

i,num1,num2 = 0,1,1

fibo_list = [] # 初始化fibo列表

while i < user_input:
    fibo_list.append(num1)

    num1,num2 = num2,num1+num2

    i += 1

print(fibo_list)

