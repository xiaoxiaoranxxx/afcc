from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
from time import sleep
import os
import time
import random
n = 0


def task1():
    while True:
        print('任务1...', os.getpid(), '------', os.getppid())
        sleep(1)


def task2():
    while True:
        print('任务2...', os.getpid(), '------', os.getppid())
        sleep(2)


if __name__ == '__main__':
    print(os.getpid())
    p = Process(target=task1, name='任务1开始...')
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2开始...')
    p1.start()
    print(p1.name)
    while True:  # 多进程能共享全局变量
        n += 1
        sleep(0.2)
        if n == 5:
            p.terminate()
            p1.terminate()
            break
        else:
            print('----->', n)
    print('*******')
    print('over')
    print()
# 进程池


def task3(task_name):
    print('任务名', task_name)
    start = time.time()
    time.sleep(1)
    end = time.time()
    print('完成用时:', (end - start), '进程id:', os.getpid())
    # return '完成用时:', (end - start),'进程id:',os.getpid()
#container = []
# def callback_func(n):
    # container.append(n)
# pool.apply_async(task3,args=(i),callback=callback_func)


if __name__ == '__main__':
    pool = Pool(5)
    task4 = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in task4:
        pool.apply_async(task3, args=(i))  # 非阻塞式
    pool.close()
    pool.join()  # 保留主进程以子进程...
    print('over')
if __name__ == '__main__':
    pool = Pool(5)
    task4 = ['1', '2', '3', '4', '5', '6', '7', '8']
    for i in task4:
        pool.apply(task3, args=(i))  # 阻塞式  一个一个上
    pool.close()
    pool.join()  # 保留主进程以子进程...
    print('over')

# 进程的通信
q = Queue(5)
q.put('1')
q.put('2')  # 放
q.put('3')
q.put('4')
q.put('5')
print(q.qsize())
if not q.full():
    q.put('6', timeout=3)
else:
    print('fulling')


def download(q):
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    for image in images:
        print('downloading', image)
        sleep(1)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功...'.format(file))
        except:
            print('ok...')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print('------------->')
#多线程
import threading
def downloade(n):
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    for image in images:
        print('downloading', image)
        sleep(n)
        print('succssful..')
n=1
def listening():
    musics = ['1','2','3','4']
    for music in musics:
        sleep(1)
        print('正在听音乐...',music)

if __name__ == '__main__':

    t = threading.Thread(target=downloade,name='xiao',args=(1,))
    t.start()
    t1 = threading.Thread(target=listening,name='xiao')
    t1.start()

    # while True:
    #     print(n)
    #     sleep(2)
    #     n +=1

#多线程可共享全局变量
money = 1000
def run1():
    global money
    for i in range(10):
        money -=1
        sleep(0.5)
        print('run1',money)
def run2():
    global money
    for i in range(10):
        money -=1
        sleep(0.5)
        print('run2',money)
if __name__ == '__main__':

    th1 = threading.Thread(target=run1,name='th1')    
    th2 = threading.Thread(target=run2,name='th2')
    th2.start()
    th1.start()
    th1.join()
    th2.join()
    print('lasting',money)

#线程同步,保证数据匹配错误
#计算密集型会自动解锁

lock =threading.Lock()
list1 = [0] * 10
def task1():
    lock.acquire()  #阻塞,等待释放
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.1)
    lock.release()
def task2():
    lock.acquire()  
    for i in range(len(list1)):
        print('------->',list1[i])
        print()
        print('<-------',i)
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    #t1.start()
    t1.join()
    t2.join()
    print(list1)

#死锁

#线程间的通信... 生产者与消费者
#sleep时间差
#Queue

#协程(微线程) 建立在 类 生成器

def taske1():   #交替执行
    for i in range(5):
        print('A'+str(i))
        yield
        time.sleep(0.1)
def taske2():
    for i in range(5):
        print('Q'+str(i))
        yield
        time.sleep(0.1)
if __name__ == '__main__':
    g1 = taske1()
    g2 = taske2()
    while True:
        try:
            next(g1)
            next(g2)
        except:
            break



from greenlet import greenlet  #秀协程
def a():   #
    for i in range(5):
        print('A'+str(i)) 
        gb.switch()      #实现交叉完成
        time.sleep(0.1)
def b():
    for i in range(5):
        print('B'+str(i))   
        gc.switch()   
        time.sleep(0.1)
def c():
    for i in range(5):
        print('C'+str(i))
        ga.switch()      
        time.sleep(0.1)

if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)
    ga.switch()
    gb.switch()
    gc.switch()

#gevent
#猴子补丁




