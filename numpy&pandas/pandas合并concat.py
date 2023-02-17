# -*-coding:utf-8-*-

import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

print(df1)
print(df2)
print(df3)

print("竖向合并 修复序号")
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# join ['inner','outer']
print("join ['inner','outer']")
df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[3, 4, 5])
print(df4)
print(df5)
res1 = pd.concat([df4, df5], join='inner')
res2 = pd.concat([df4, df5], join='outer')
print(res1)
print(res2)

# join_axes 弃用
# df6 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
# df7 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# res = pd.concat([df6,df7],axis=1,join_axes=[df6.index])
# print(res)

# append 也可以添加一条序列
df8 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df8.append(s1,ignore_index=True)
print(res)
