# -*-coding:utf-8-*-
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = np.array([[1, 1], [1, 0]])

print(a, b)

# array的加减乘除法
c = a - b
print(c)

# 乘方
c = b ** 2
print(c)

# 其他函数
c = np.sin(a)
print(c)

# 向量内元素比较大小
# [0 1 2 3]
# [ True  True  True False]
print(b)
print(b < 3)

c = np.array([[1, 1], [1, 0]])
d = np.arange(4).reshape((2, 2))

print("乘法实验")
print(c)
print(d)

# 矩阵乘法 与 普通乘法的不同
print(c * d)
print(np.dot(c, d))

# 创建随机array
a = np.random.random((2, 4))
print(a)

# array自身运算（总和，最大小值等）
print(np.sum(a))
print(np.min(a))
print(np.max(a))

# 要求array行的自身运算，则要指定axis=1
# 一句话看懂axis：设axis=i ,则numpy沿着第i个下标变化的方向进行操作

# 输入
# [[0.34434839 0.24124617 0.23013321 0.50940957]
# [0.83646653 0.24990892 0.75642396 0.51718354]]
# 输出
# [0.50940957 0.83646653]

print(np.max(a,axis=1))