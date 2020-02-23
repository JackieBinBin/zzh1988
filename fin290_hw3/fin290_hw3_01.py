import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# a. Generate a random sequence of 25 values between 0 and 100 and
# place them into a Pandas data frame.
# return <class 'numpy.ndarray'>

random_sequence = np.random.randint(101,size=25)

random_sequence_df = pd.DataFrame(random_sequence)

# b. Using the plotting tools plot the data as a time series.

random_sequence_df.plot(title='fin290_hw3_01_b_case')
plt.show()

# c. Find 2 stocks of your choice and place 25 days of the values of each day
# of the stock into a Pandas data frame and plot both as a time series.

stocks = {'Tesla':[780,791.1,801,802.45,800.43,858.4,878,895.46,910.83,920,905.88,911,
                   875,874,873,872,899,855,844,833,822,711.43,1001,777,775],
          'Sina':[880,891.1,701,702.45,600.43,658.4,578,595.46,710.83,320,905.88,911,
                   675,674,673,672,699,655,644,633,822,711.43,1001,777,775]}

stocks_df = pd.DataFrame(stocks,columns=['Tesla','Sina'])

stocks_df.plot(title='fin290_hw3_01_c_case')
plt.show()

