#  Give 2 examples of objects in python that are mutable and two that are not?

# python中不可变数据类型的定义为：当该数据类型的对应变量的值发生了改变，
# 那么它对应的内存地址也会发生改变，就称不可变数据类型
# 包括：int（整型）、string（字符串）、tuple（元组）

girl = 100
# 打印girl的内存地址和数据类型
print(id(girl), type(girl))

# 输出：140713680622336 <class 'int'>


# 改变x的值
girl = 101
# 打印改变后的x的内存地址和数据类型
print(id(girl), type(girl))

# 输出：140713680622368 <class 'int'>

# python中对可变数据类型的定义为：当该数据类型的对应变量的值发生了改变，
# 那么它对应的内存地址不发生改变，就称可变数据类型。
# 包括：set（集合）、list（列表）、dict（字典）

list_zzh = [1, 2, 3, 4, 5]
print("列表:", list_zzh, "内存地址：", id(list_zzh), "\t", "数据类型：", type(list_zzh), "\t")
# 输出：列表: [1, 2, 3, 4, 5] 内存地址： 1439217744000 	 数据类型： <class 'list'>

list_zzh[0] = 250
print("列表:", list_zzh, "内存地址：", id(list_zzh), "\t", "数据类型：", type(list_zzh), "\t")
# 输出：列表 [250, 2, 3, 4, 5] 内存地址： 1439217744000 	 数据类型： <class 'list'>