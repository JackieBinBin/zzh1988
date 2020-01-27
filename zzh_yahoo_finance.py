import pandas as pd
import pandas_datareader.data as pdr


# prices = pdr.DataReader('AAPL', 'yahoo', start='2010-01-01')

# print(prices)

# new_prices = prices.drop(['High'], axis=1)


data = pd.read_excel('Class3_hisassetret.xlsx',parse_dates=[1])

# 打印每列的类型
print(data.dtypes)

# data['Year'] = pd.to_datetime(data['Year'])

# print(data['Year'])

# 将Year设置为索引 index 类似于图书目录

# data.index = data['Year']
# print(data.index)

# 根据Year 属性，根据条件，提取一个新的数据表，
zzh = (data['Year'] > 1950) & (data['Year'] < 2000)

print(data[zzh])


# 公式

# prices['simple_return'] = (prices['Adj Close']/prices['Adj Close'].shift(1)-1)


# print(prices['simple_return'].head(10))

# print('---------获取某月的数据-----------')
# print(prices['2012-11']) # 获取某月的数据

# 根据公式换算出来的结果，按月统计数据
# Resample ： 根据指定的时序统计数据

# prices_M = prices['simple_return'].resample('M').sum()
#
# print(prices_M.head(10))