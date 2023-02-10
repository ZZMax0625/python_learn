#-*-coding:utf-8-*-

import threading
import time


# threading.Event()
# 通过threading.Event()可以创建一个事件管理标志，该标志（event）默认为False，event对象主要有四种方法可以调用：
#
# event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行；
# event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒
# event.clear()：将event的标志设置为False，调用wait方法的所有线程将继续被阻塞
# event.isSet()：判断event的标志是否为True

def find_log():
    i = 0
    while True:
        time.sleep(0.5)
        if i > 10:
            print('find log')
            event.set()
            break
        i += 1


if __name__ == '__main__':
    event = threading.Event()
    threading.Thread(target=find_log).start()
    print('wait log')
    event.wait()  # 等待到event.set()在继续往下执行
    print('start processing log')
    pass
