# write python code to output the elements in d sequentially.
# i.e. your code should output the sea creatures element by element first
# and then the numbers 1, 2, ... to 5 and so on.

L = ['mako', 'beluga', 'narwhal','great white','killer whale']
d = {'sea creatures':L, 1: [1, 2, 3, 4, 5], 'two':[f'{i}' for i in range(10,21)]}

# print(d)


for i in d.keys(): # 遍历字典d对应的key信息
    for j in d[i]:
        print(j,end=' ')

#输出结果：mako beluga narwhal great white killer whale 1 2 3 4 5 10 11 12 13 14 15 16 17 18 19 20


