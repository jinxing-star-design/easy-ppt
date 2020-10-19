import threading  #多线程
import time
def add(x,y):
    print('entering this thread.')
    time.sleep(3)
    print(x+y)
    print('=========end')

t = threading.Thread(target=add, args=(4,5)) #当目标函数启动起来时，传什么参数：4，5
t.start()

print('~~~~~~~~~~~~~~')



