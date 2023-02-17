# -*-coding:utf-8-*-

import pandas as pd

# 从csv读取
data = pd.read_csv('student.csv')

print(data)

# 导出
data.to_pickle('student.pickle')


