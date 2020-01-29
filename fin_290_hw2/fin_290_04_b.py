prime_num = []

user_num = int(input('Please input a integer N: '))

for i in range(2,user_num+1):
    for j in range(2,i): # 逻辑：从2-i区间遍历数据，要保证区间内均不能整除
        if (i%j == 0):   # 表明能被除自身外的数字整除，非质数
            break
    else:
        prime_num.append(i)

# 上述 for ...else 循环体执行逻辑为：
# 在for循环完整！！完成！！后才执行else；如果中途从break跳出，则连else一起跳出

print(prime_num)