# -*-coding:utf-8-*-

import pandas as pd
import numpy as np

dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

# 第二列第二行的值改为111
df.iloc[2, 2] = 111
print(df)

df.loc['20230102', 'B'] = 2345
print(df)

# A标签下大于0的行
df[df['A'] > 0] = 7
print(df)
# 只改A列
df.A[df['A'] > 4] = 8
print(df)
df['F'] = np.nan
print(df)
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20230101', periods=6))
print(df)
