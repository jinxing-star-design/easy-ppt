#reduce函数
# def partial(func,*args,**keywords):    #传入**keywords中
#     def newfunc(*frags,**fkeywords):   #传入*frags中 fargs =（4，） fkeywords = {}
#         newkeywords = keywords.copy()   #{'y':5}
#         newkeywords.update(fkeywords)  #fkeywords为空
#         return func(*args,*fargs,**newkeywords)
#     newfunc.func = func            #newfunc现在是add
#     newfunc.args = args            #newfunc函数的args值传入
#     newfunc.keywords = keywords    #传入 {'y':5}
#     return newfunc
#
# def add(x,y):
#     return x + y
# newadd = partial(add,y=5)         #newadd = newfunc
# newadd(4)                         #newfunc(4)


from functools import  reduce
print(reduce(lambda value,x : value + x ,range(5),10))
#partial函数

from functools import partial
import inspect
def add(x,y):
    return x + y

newadd = partial(add,4)
print(newadd(5))

newadd = partial(add,y = 5)
print(inspect.signature(newadd))
print(newadd(4))

newadd = partial(add,x=4,y=5)

print(newadd(x=10,y=11)) 