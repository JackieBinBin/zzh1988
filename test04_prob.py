# This is starter code for HW#1 problem #4

# for loop to sum all numbers from 1 to N
# N is input by a user

N = int(input("Please enter an integer N: "))
my_sum = 0 #initialize your sum to 0

if isinstance(N,int) and N >0:
    for i in range(1, N+1): #range function returns an iterable object
        my_sum += i #here you need to find a way to update your sum in the loop

    print(f'Sum of the numbers from 1 to {N} = {my_sum}')  # again f-string formatting
else:
    print(f'WARNING:input error: {N},num should be int and positive')


