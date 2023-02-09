#-*-coding:utf-8-*-

import numpy as np

a = np.arange(4)
print(a)

b = a
c = a
d = b

d[0] = 875

# 因为是赋值的地址，所以这四者相等

print(a)
print(b)
print(c)
print(d)

# 深拷贝
b = a.copy()
a[3] = 333

print(a)
print(b)
print(c)
print(d)