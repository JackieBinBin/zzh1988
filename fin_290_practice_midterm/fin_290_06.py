#If I execute the following operation, explains what happens to d and L and why?
#>>> d[‘list’][0] = ’first entry!!’
#If I do the following operation, what happens?
#>>> d[‘list’][4] = 999

L = [1, 2, 3, 4, 5]

d = {1:'hi', '2':'hello', 'three':3, 'list':L}

d['list'][0] = 'first entry!!'
d['list'][4] = 999

print(d)
# So from this experiment, can you conclude that dicts mutable? How’s about aliasing?
# 结合第三题看，list和dict 均为可变数据类型，所以肯定是改变了d字典内的数据值的
# 对应打印结果为：{1: 'hi', '2': 'hello', 'three': 3, 'list': ['first entry!!', 2, 3, 4, 999]}
#=======================================================================

# Suppose I want to copy the current form of dict d as a new dict called dict2
# and only change the first entry in the list to ‘2019’ without changing the
# first entry in dict d. How can I do this?

# 都copy出来了，对应的内存地址都完全不一样，肯定不得改原来dict d的数据值，不晓得我理解对了么
# 额！
