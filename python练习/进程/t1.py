import threading


def worker():
    print('I am working')
    print('finish')


t = threading.Thread(target=worker, name='worker1')
t.start()

print('=======end=============')