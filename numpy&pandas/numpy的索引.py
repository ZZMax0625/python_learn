# -*-coding:utf-8-*-

import numpy as np

A = np.arange(3, 15)
print(A)

# 拿到第三个值（从0数）
print(A[3])

# 矩阵的第n个元素
A = np.arange(3, 15).reshape((3, 4))
print(A)
print(A[1])
print(A[1][0])
# print(A[1, 0]) 同样的写法

# 用冒号代替所有数
print(A[2, :])

# 用冒号从1到2
print(A[2, 1:3])

print("循环测试")

# 迭代行
for row in A:
    print(row)

# 迭代列(通过转置的办法)
for col in A.T:
    print(col)

# 迭代元素 A.flat = A.flatten() 迭代器？ 使用reshape可行吗？
for item in A.flat:
    print(item)
