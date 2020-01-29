# fin_290_3_Clean Data
# 2、 with built in string methods.
# goal:prints the sum of the numbers in the string s

myString = '**1.23,*2.4*, 3.123,*5.1, 8.7*, *7.23, *3.23*'
s = myString.replace('*','') # 将符号'*' 替换为 空格

st_sum = '' # initialize to empty string
my_sum = 0.0 #initialize Sum = 0.0

for c in s.split(','):  #iterate over chars in string s
    #use conditionals to extract numbers in the string
    my_sum += float(c)
    # print(c)
print(f'The sum of the numbers in {myString} is {my_sum}')