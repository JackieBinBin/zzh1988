# Use list comprehension to create a numpy array of elements
# containing the numbers from 1 to 100.

import numpy as np

numpy_array = np.array([i for i in range(1,101)]) # 因为题目强调要用numpy array

# print(numpy_array)
# print(type(numpy_array))

# ? python list array 和 numpy 里面array区别

#  In one line, write code to reverse it;

numpy_array_reverse = numpy_array[::-1] # [::-1]代表反序

print(numpy_array_reverse)

#  Do the same for a list and reverse it by 2 methods.



# reverse method 1:

array_list1 = [i for i in range(1,101)]

array_list1.reverse()

print(f'Method 1 reverse list :  {array_list1}')

# reverse method 2:

array_list2 = [i for i in range(1,101)]

array_list2 = sorted(array_list2,reverse=True)

print(f'Method 2 reverse list :  {array_list2}')