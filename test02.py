# -*- coding:utf-8 -*-

x=666; y=-777; z=888

print(f'org list:x = {x},y = {y},z = {z}')

# 01：排序,从小到大；

if x > y:
    x,y=y,x
if y > z:
    y,z=z,y
if x > y:
    x,y=y,x

print(f'convert list:x = {x},y = {y},z = {z}')

# 02：找最大奇数：

if z%2==0: # z is even
    if y%2==0: #y is even
        if x%2==0: # x is even
            print(f'WARNING: no odd num!!!!!')
        else:
            print(f'x = {x} is largest odd!!')
    else:
        print(f'y = {y} is largest odd!!')
else:
    print(f'z = {z} is largest odd!!')
