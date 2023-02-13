# -*-coding:utf-8-*-
from enum import Enum

import numpy as np


# print("hello world")
#
# print("test")
#
# print(0xe == 14)

class Areas(Enum):
    PE = 0x81
    PA = 0x82
    MK = 0x83
    DB = 0x84
    CT = 0x1C
    TM = 0x1D


print(0x84 in Areas)
