# -*-coding:utf-8-*-

from functools import lru_cache
import matplotlib.pyplot as plt
import time
import math
import datetime


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(n):
    if n == 3:
        return True
    if n == 1 or n == 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


end = 1000001
per = int(end / 5)
prime_list = []
index_list = []
x_list = range(0, end-1, per)
y_list = []
count = 0
count_prime = 0

for item in range(1, end):
    count = count + 1
    if is_prime(item):
        count_prime = count_prime + 1
        prime_list.append(item)
        index_list.append(item)
    if count >= per:
        y_list.append(count_prime)
        count = 0
        count_prime = 0

print(len(y_list))
for item in y_list:
    print(item)
print(len(y_list))

# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 画图，plt.bar()可以画柱状图
plt.bar(x_list, y_list,width=int(end/100))
# for i in range(len(x_data)):
#     plt.bar(x_data[i], y_data[i])

# 设置图片名称
plt.title("分析")
# 设置x轴标签名
plt.xlabel("范围")
# 设置y轴标签名
plt.ylabel("个数")
# 显示
plt.show()

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
# plt.figure(figsize=(20, 10), dpi=100)
# # game = ['1-G1', '1-G2', '1-G3', '1-G4', '1-G5', '2-G1', '2-G2', '2-G3', '2-G4', '2-G5', '3-G1', '3-G2', '3-G3',
# #         '3-G4', '3-G5', '总决赛-G1', '总决赛-G2', '总决赛-G3', '总决赛-G4', '总决赛-G5', '总决赛-G6']
# # scores = [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 34, 33, 25, 28, 40, 28]
# # plt.plot(range(1, len(prime_list) + 1), prime_list)
# plt.scatter(index_list, prime_list, edgecolors='r', s=0.1)
#
# plt.show()

# start_time = time.time()
# print(fibonacci(40))
# end_time = time.time()
#
# print("耗时：" + str(end_time - start_time))
