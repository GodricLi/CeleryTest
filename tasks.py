# _*_ coding=utf-8 _*_
from __future__ import absolute_import

import time
from celery import Celery

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'
app = Celery('my_tasks', broker=broker, backend=backend)


@app.task
def add(x, y):
    print('enter task')
    time.sleep(3)
    return x + y


if __name__ == '__main__':
    result = add.delay(10, 20)
