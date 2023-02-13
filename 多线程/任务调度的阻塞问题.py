#-*-coding:utf-8-*-

from apscheduler.schedulers.background import BackgroundScheduler

import time

# 非阻塞任务中，任务时长超出间隔时长的情况
def job():

    print('job 3s')

    time.sleep(5)

if __name__=='__main__':

    sched = BackgroundScheduler(timezone='MST')

    sched.add_job(job, 'interval', id='3_second_job', seconds=3)

    sched.start()

    while(True):

        print('main 1s')

        time.sleep(1)