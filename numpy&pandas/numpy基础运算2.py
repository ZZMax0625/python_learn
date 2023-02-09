# -*-coding:utf-8-*-
import numpy as np

A = np.arange(2, 14).reshape((3, 4))
print(A)

# 获取最小/大值索引
print(np.argmin(A))

# 矩阵平均值,中位数等统计信息
print(np.mean(A))

# 矩阵累加过程 (前缀和差分)
# 输入
# [[ 2  3  4  5]
#  [ 6  7  8  9]
#  [10 11 12 13]]
# 输出
# [ 2  5  9 14 20 27 35 44 54 65 77 90]
print(np.cumsum(A))

# 除了累加还有两个元素之间的差的矩阵
print(np.diff(A))

# 返回非0索引
print(np.nonzero(A))

# 排序(只能正序)
print(np.sort(A))

# 矩阵转置
print(np.transpose(A))
# print(A.T) 是一样的

# 矩阵所有小于5的数都变成5，大于9的数变成9，其余不变（滤波？限幅？）
print(np.clip(A, 5, 9))

# 矩阵按列/行求平均
print(A)
print(np.mean(A, axis=1))
