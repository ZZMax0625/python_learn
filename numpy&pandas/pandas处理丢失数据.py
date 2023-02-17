# -*-coding:utf-8-*-
import pandas as pd
import numpy as np

dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

# 数据出现缺省
print("数据缺省")
print(df)
# 丢掉行
print("丢掉行 how里面有any all")
print(df.dropna(axis=0, how='any'))

# 补全
print("用特定数字补全")
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.fillna(value=0))

# 检查Null值
print("检查Null值")
print(df.isnull())

