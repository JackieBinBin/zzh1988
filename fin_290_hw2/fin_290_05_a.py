
# The lazy way
# import numpy as np
#
# a = [52,69,35,65,89,15,34]
# b = np.mean(a)
# c = np.median(a)
# print(b)
# print(c)

######################################

N = int(input('Please input a interger number: '))

# Generate a random list of numbers of length N
import numpy as np

# 通过numpy的randint方法，生成100内的随机数 N个，返回为数组类型
# tolist 方法，把数组转为list
# 这里都假设是int整数型，如果要小数，用：np.random.randn(10)
random_list = np.random.randint(100,size=N).tolist()

# verify list
# print(random_list)
# print(len(random_list))

# Calculate the mean of the number in list:
# 即算平均数 Average
sum = 0

for i in random_list:
    sum +=i

random_list_mean = sum/len(random_list)

print(f' The mean of the number from the random_list is : {random_list_mean} ')

# Calculate the median of the number in list:即中位数
# 1、先排序，从小到大，或者是从大到小。然后去取中间的值；
# 2、对奇数数列，取中间，
# 3、对偶数数列，把中间的两个数找到，计算这两个数的mean,也就是他们的平均值（算术平均值）

random_list.sort()

midpos = len(random_list)//2 # 这里取整，略小数

print(midpos)

if len(random_list) %2 == 0: #偶数队列
    random_list_median = (random_list[midpos] + random_list[midpos-1])/2
else:# 奇数队列
    random_list_median = random_list[midpos]

print(f' The Median of the number from the random_list is : {random_list_median} ')

