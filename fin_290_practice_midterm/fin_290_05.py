# Using list comprehension, do the same as in problem 4 except without explicitly
# using the lists L1 and L2.
# 即列表推导式

L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]

square_L1 = [i*i for i in L1]

double_L2 = [j*2 for j in L2]

L3 = [ i+j for i in square_L1 for j in double_L2 if square_L1.index(i) == double_L2.index(j)]

print(L3)