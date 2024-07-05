from jqdatasdk import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/000001-XSHE_2023-03-28_2024-04-03.csv')

strategy = pd.DataFrame(index = df.index)

strategy['signal'] = 0

strategy['avg_5'] = df['close'].rolling(5).mean()
strategy['avg_10'] = df['close'].rolling(10).mean()

strategy['signal'] = np.where(strategy['avg_5'] > strategy['avg_10'], 1, 0)

strategy['order'] = strategy['signal'].diff()

# 画图
plt.figure(figsize=(10, 5))

plt.plot(df['close'], lw=2, label='price')

plt.plot(strategy['avg_5'], lw=2, ls='--', label='avg_5')

plt.plot(strategy['avg_10'], lw=2, ls='-.', label='avg_10')

plt.scatter(strategy.loc[strategy.order == 1].index,
            df['close'][strategy.order == 1],
            marker = '^', s=80, color='r', label='Buy')

plt.scatter(strategy.loc[strategy.order == -1].index,
            df['close'][strategy.order == -1],
            marker = 'v', s=80, color='g', label='Sell')

plt.legend()

plt.grid()
plt.show()

# 回测
initial_cash = 20000

positions = pd.DataFrame(index = strategy.index).fillna(0)

positions['stock'] = strategy['signal'] * 100

portfolio = pd.DataFrame()
portfolio['stock value'] = positions.multiply(df['close'], axis=0)

order = positions.diff()

portfolio['cash'] = initial_cash - order.multiply(df['close'],
                                                 axis=0).cumsum()

portfolio['total'] = portfolio['cash'] + portfolio['stock value']
#检查一下后10行
print(portfolio.tail(10))

#创建10*5的画布
plt.figure(figsize=(10,5))
#绘制总资产曲线
plt.plot(portfolio['total'], lw=2, label='total')
#绘制持仓股票市值曲线
plt.plot(portfolio['stock value'],lw=2,ls='--', label='stock value')
#添加图注
plt.legend()
#添加网格
plt.grid()
#展示图像
plt.show()