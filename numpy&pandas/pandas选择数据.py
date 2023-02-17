# -*-coding:utf-8-*-
import pandas as pd
import numpy as np


# DataFrame 的构造主要依赖如下三个参数：
#
# data：表格数据；
# index：行索引；
# columns：列名；
# index 对行进行索引，columns 对列进行索引

dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# 取第A列
print(df['A'])
# print(df.A) 和上述代码功能一致

print("数据选择")
# 数据选择0:3 是指0到3位，后面的是指列
print(df[0:3], df['2023-01-02':'2023-01-04'])

# 标签选择语句 loc
print(df.loc['2023-01-04'])
print(df.loc['2023-01-02', ['A', 'B']])

# 位置选择语句 iloc
print("位置选择语句 iloc")
print("第三行的数据(从0索引)")
print(df.iloc[3])
print("第三行第一位")
print(df.iloc[3, 1])
print("第三到第五行，第一列到第三列")
print(df.iloc[3:5, 1:3])
print("行上的逐个筛选")
print(df.iloc[[1, 3, 5], 1:3])

# 混合筛选 已弃用
print("混合筛选")
# print(df.ix[:2, ['A', 'C']])

# boolean indexing
print("大于8的部分")
print(df[df.A > 8])
