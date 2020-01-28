prime_num = []

for i in range(2,101):
    for j in range(2,i): # 逻辑：从2-i区间遍历数据，要保证区间内均不能整除
        if (i%j == 0):   # 表明能被除自身外的数字整除，非质数
            break
    else:
        prime_num.append(i)

print(prime_num)