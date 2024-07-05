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

plt.figure(figsize=(10, 5))

plt.plot(df['close'], lw=2, label='price')

plt.plot(strategy['avg_5'], lw=2, ls='--', label='avg_5')

plt.plot(strategy['avg_10'], lw=2, ls='-.', label='avg_10')

plt.scatter(strategy.loc[strategy.order == 1].index,
            df['close'][strategy.order == 1],
            marker = '^', s=80, color='r', label='Buy')

plt.scatter(strategy.loc[strategy.order == -1].index,
            df['close'][strategy.order == -1],
            marker = 'v', s=80, color='r', label='Sell')

plt.legend()

plt.grid()
plt.show()