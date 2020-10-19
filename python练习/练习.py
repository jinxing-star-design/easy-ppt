import time
from functools import wraps


def outter(func):
    @wraps(func)
    def wrapper(x, y):
        start = time.time()
        res = func(x, y)
        stop = time.time()
        print(stop-start)
        return res
    return wrapper


@outter #index=outter(index)
def index(x, y):
    print('index %s %s' % (x, y))
    time.sleep(3)



#index = outter(index)

index(1, 2) #其实执行的是wrapper(1,2)