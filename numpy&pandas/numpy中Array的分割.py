# -*-coding:utf-8-*-

import numpy as np

A = np.arange(12).reshape((3, 4))

print(A)

# 分割
print(np.split(A, 2, axis=1))

# 纵/横向分割
print(np.vsplit(A, 3))
print(np.hsplit(A, 2))
