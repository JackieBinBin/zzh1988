import pandas as pd
import pandas_datareader.data as pdr

prices = pdr.DataReader('AAPL', 'yahoo', start='2010-01-01')

# 公式

prices['simple_return'] = (prices['Adj Close']/prices['Adj Close'].shift(1)-1)

print(prices['simple_return'].head(40))

# print('---------获取某月的数据-----------')
# print(prices['2012-11']) # 获取某月的数据

# 根据公式换算出来的结果，按月统计数据
# Resample ： 根据指定的时序统计数据

prices_M = prices['simple_return'].resample('M').sum()

print(prices_M.head(10))
