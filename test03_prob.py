# This is starter code for HW#1 problem #3

myString = '1.23, 2.4, 3.123'
s = myString

st_sum = '' # initialize to empty string
my_sum = 0.0 #initialize Sum = 0.0

for c in s:  #iterate over chars in string s
     # use conditionals to extract numbers in the string
    if  c != ',':
        st_sum += c # 这里一直在做字符串拼接，直到遇到,字符串，再先行求和
    else:
        my_sum += float(st_sum) # 直到遇到,字符串，再先行求和
        st_sum = '' # 置位空，再继续拼接下一个逗号前的字符串

my_sum += float(st_sum) # 这里加了最后一个逗号后面的数字

print(f'The sum of the numbers in {myString} is {my_sum}')

