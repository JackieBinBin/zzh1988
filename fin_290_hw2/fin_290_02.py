# About the Monty Hall Problem, Do 10 millions trials and
# calculate the experimental probability in each case (swap or not)

import random

doors = ['goat','goat','benz_car']

swap_win = 0 # 交换成功次数统计
swap_lose = 0 # 交换失败次数统计


# 定义循环100万次，统计每次交换成功和失败的次数
# 每次做到观众纯随机选择
# 每次做到door纯随机道具布置
iterations = 1000000

for i in range(iterations):

    random.shuffle(doors) # 每次都纯随机道具布置

    # 观众小张随机选择门 a
    zzh_choice = random.randrange(3) #randrange()返回0-2集合中的一个随机数，来模拟观众选择

    # 主持人Monty选择门 b:b!=a 且 doors[b] != 'benz_car'
    # 主持人只会选择有goat的门，所以这里不需要代码实现也可以


    # 在小张选择换门的前提下，判断选择成功或者失败：
    if doors[zzh_choice] == 'benz_car':
        swap_lose += 1
    else: # 基于上述逻辑，门c肯定就是车车
        swap_win += 1


print(f'循环100万次，选择换门，成功次数为：{swap_win}，对应成功率为：{100*swap_win/iterations}%')
print(f'循环100万次，不选择换门，成功次数为：{swap_lose}，对应成功率为：{100*swap_lose/iterations}%')
print(f'综上，不管多次循环还是重新100万次执行，换门的胜率无限趋近于在2/3,不换只有趋近于1/3')




