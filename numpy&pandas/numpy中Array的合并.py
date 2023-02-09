# -*-coding:utf-8-*-

import numpy as np

# 花里胡哨的各种合并

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# 上下合并
print(np.vstack((A, B)))

# 左右合并
print(np.hstack((A, B)))

# 转成单个列元素组成的竖向矩阵
print("转竖")
print(A)
print(A.shape)

# 在行上加一个维度
print(A[np.newaxis, :])
print(A[np.newaxis, :].shape)
# 在列上加一个维度
print(A[:, np.newaxis])
print(A[:, np.newaxis].shape)

print("指定维度合并")

# 多个合并，指定维度
A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
print(A)
print(B)
C = np.concatenate((A, B, B, A), axis=1)

print(C)
