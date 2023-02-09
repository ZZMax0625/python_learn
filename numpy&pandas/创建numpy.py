# -*-coding:utf-8-*-
import numpy as np

# 通过list创建 array的type叫做dtype
a = np.array([[2, 23, 4], [3, 4, 5]], dtype=np.int)
# a = np.array([2, 23, 4], dtype=np.float)

# 里面的元素为什么类型 int默认是32位，可改为int64
print(a.dtype)

# 可以发现没有逗号分隔列表
print(a)

# 创建0矩阵
b = np.zeros((3, 4))
print(b)

# 创建1矩阵
c = np.ones((3, 4), dtype=int)
print(c)

# 创建有序的矩阵,起始位，终点，步长
d = np.arange(10, 20, 2)
print(d)

# 创建有序的,自定义shape的矩阵,起始位，终点，步长
e = np.arange(12).reshape((3, 4))
print(e)

# 生成线段(1到10，分成20段),也可以reshape
f = np.linspace(1, 10, 20)
print(f)

