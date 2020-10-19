import time
import datetime
from functools import wraps, update_wrapper


def timeit(fn):
    #@wraps(fn) #wrapper = wraps(fn)(wrapper)
#fn里存储着旧的add，也就是执行x+y的函数，返回的函数wrapper赋给了timeit
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs) #带了括号才是调用
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s.'.format(fn.__name__, delta))
        return ret
    return wrapper
@timeit  #timeint = timeint(add)
def add(x, y):
    time.sleep(2)
    return x + y


print(add(4, 5)) #相当于wrapper(4, 5)
#with TimeIt(add):
