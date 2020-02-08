# Using a lambda and functional programming,
# sum the squares of the first list to double of the second
#list and place those into a new list called L3:
#L1 = [1, 2, 3, 4, 5] and L2 = [6, 7, 8, 9, 10]
#e.g. the first entry should be 1^2 + 2 ∗ 6

L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]

square_L1 = map(lambda x:x*x,L1) # map函数为针对L1每个元素，进行求平方

double_L2 = map(lambda x:x*2,L2) # 同上

L3 = map(lambda x,y:x+y,square_L1,double_L2) # L1 L2同位置 相加

print(list(L3))
