# _*_ coding=utf-8 _*_

from tasks import add

if __name__ == '__main__':
    print('start task')
    result = add.delay(3, 18)
    print('end task')
    print(result)
