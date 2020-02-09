#  Debugging

#(a) When I try to to type the following, I get an error message.
# What is going on with my code?
#>> x = ‘1,2,3,4,5,’
#>> x[-1] = 6
#>> print(x[-1])

# 这里定义的x是数组的嘛，肯定错的撒 要转为列表类才行

#(b) Find the bug(s) if any in the following code and fix if possible:
#def f(x):
#return x^2 + 2*x - 2
#x0 = 1
#for i in range(10)
#x1 = f(x0)**2 - x0
#print(x) = x1  -----> 看不懂
#x0 = x1

def f(x):
    return x^2 + 2*x - 2
x0 = 1
for i in range(10):
    x1 = f(x0)**2 - x0
    print(x1)
    x0 = x1
