# This is starter code for HW#1 problem #3

# myString = '1.23, 2.4, 3.123'
# s = myString
#
# st_sum = '' # initialize to empty string
# my_sum = 0.0 #initialize Sum = 0.0
#
# for c in s:  #iterate over chars in string s
#     #use conditionals to extract numbers in the string
#     my_sum += float(c)
#     # print(c)
# print(f'The sum of the numbers in {myString} is {my_sum}')

# myString 带空格  '1.23, 2.4, 3.123'


myString = '1.23, 2.4, 3.123'
s = myString

st_sum = '' # initialize to empty string
my_sum = 0.0 #initialize Sum = 0.0

for c in s.split(','):  #iterate over chars in string s
    #use conditionals to extract numbers in the string
    my_sum += float(c)
    # print(c)
print(f'The sum of the numbers in {myString} is {my_sum}')