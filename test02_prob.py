# This is starter code for HW#1 problem #2
# Code uses only conditionals as instructed
# Code does use f-strings which will be talked about in lecture on 1/16
# The starter code only deals with the case when x is even
# you will need to handle the case when x is odd in a similar manner

x = 10; y = 9; z = 9; #base test case
# x = -10; y = 2; z = -7 #more interesting case to test
#inline commands can be separated by semi-colons

print(f'x = {x}, y = {y}, z = {z}') #print out the values of x, y, and z

if x%2 == 0:  # x even
    if y%2 == 0:  # y even
        if z%2 == 0:  # z even
            print('no odd numbers in list')
        else:  # z odd
            print(f'z = {z} is largest odd')
    else:  # y odd
        if z%2 != 0: # z odd
            if y > z:
                print(f'y = {y} largest odd')
            else: # 这里如果y z 相等，那么y z 都是最大odd 才对，这里逻辑有问题
                print(f'z = {z} is largest odd')
        else: # z even
            print(f'y = {y} is largest odd')
else:   # x odd. You will need to finish this case with conditionals
        # you will need to inspect the cases when y and z are even or odd
        # and branch accordingly
    if y%2 == 0: # y even
        if z%2 == 0: # z even
            print(f'x = {x} largest odd')
        else: # z odd
            if x > z:
                print(f'x = {x} largest odd')
            else:
                print(f'z = {z} largest odd')
    else: # y odd
        if z%2 == 0:# z even
            if x > y:
                print(f'x = {x} largest odd')
            else:
                print(f'y = {y} largest odd')
        else:# z odd
            if x > y and x > z:
                print(f'x = {x} largest odd')
            elif y > x and y > z:
                print(f'y = {y} largest odd')
            else:
                print(f'z = {z} largest odd')



