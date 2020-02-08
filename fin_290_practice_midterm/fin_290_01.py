# Using a ‘while loop’, write python code that sums all the cubes of numbers from 1 to N,
# where N is input by a user

user_input = int(input(f'Please input a number N: '))

step = 0
sum = 0

while step <= user_input: # 从0-N做累加
    sum += step
    step += 1

print(f'The sum of input number is: {sum}')


