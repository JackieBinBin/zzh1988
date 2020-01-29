# fin_290_3_Clean Data
# 1、without using any built in functions or methods associated
# to the string object but with a for or while loop
# goal:prints the sum of the numbers in the string s


myString = '**1.23,*2.4*, 3.123,*5.1, 8.7*, *7.23, *3.23*'
s = myString

st_sum = '' # initialize to empty string
my_sum = 0.0 #initialize Sum = 0.0

for c in s:  #iterate over chars in string s
     # use conditionals to extract numbers in the string
    if   c == '*': # 过滤掉符号：*
        continue   # 终止本次循环，进行下一次循环
    elif c != ',':
        st_sum += c  # 这里一直在做字符串拼接，直到遇到,字符串，再先行求和
    else:
        my_sum += float(st_sum) # 直到遇到,字符串，再先行求和
        st_sum = '' # 置位空，再继续拼接下一个逗号前的字符串

my_sum += float(st_sum) # 这里加了最后一个逗号后面的数字

print(f'The sum of the numbers in {myString} is {my_sum}')