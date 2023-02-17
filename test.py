# -*-coding:utf-8-*-

from functools import lru_cache
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
        print(i)
        if n % i == 0:
            return False
    return True

print(int(math.sqrt(fibonacci(94))))

# prime_list = []
# for item in range(94, 95):
#     print(item)
#     fibonacci_value = fibonacci(item)
#     print(fibonacci_value)
#     if is_prime(fibonacci_value):
#         prime_list.append(
#             {
#                 "fibonacci_index": item,
#                 "fibonacci_value": fibonacci_value
#             }
#         )
#
# print(prime_list)


# start_time = time.time()
# print(fibonacci(40))
# end_time = time.time()
#
# print("耗时：" + str(end_time - start_time))
