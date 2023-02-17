# -*-coding:utf-8-*-
import pandas as pd
import numpy as np

# 序列
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

# 日期序列
dates = pd.date_range('20230217', periods=6)
print(dates)

# 默认的行列序列为0 1 2 。。。
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(['test', 'train', 'test', 'test']),
                   'F': 'foo'
                   })
print(df)
print(df.columns)
print(df.values)

# 描述只针对数字信息
print(df.describe())


