from jqdatasdk import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

auth('账号','密码')

period = 10

avg_10 = []

avg_value = []

df = pd.read_csv('data/000001-XSHE_2023-03-28_2024-04-03.csv')

for price in df['close']:
    avg_10.append(price)
    
    if len(avg_10) > period:
        del avg_10[0]
    
    avg_value.append(np.mean(avg_10))
    
# df.assign(avg_10 = avg_value)
# print(pd.Series(avg_value, index = df.index))
df['avg_10'] = pd.Series(avg_value, index = df.index)

plt.figure(figsize=(10,6))
plt.plot(df['close'], lw=2, c='k')

plt.plot(df['avg_10'], '--', lw=2, c='b')

plt.legend()
plt.grid()

plt.show()