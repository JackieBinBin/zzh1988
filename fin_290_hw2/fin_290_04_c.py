prime_num = []

user_num = int(input('Please input a integer N: '))

for i in range(2,user_num+1):
    for j in range(2,i): # 逻辑：从2-i区间遍历数据，要保证区间内均不能整除
        if (i%j == 0):   # 表明能被除自身外的数字整除，非质数
            break
    else:
        prime_num.append(i)

# 思路：1、先根据指定的区间，把质数列表提取出来，获取到：prime_num
#       2、 用列表推导式咯~

twins_primes = [(p, p+2) for p in prime_num if p+2 in prime_num]

print(twins_primes)