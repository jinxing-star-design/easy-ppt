#判断用户输入的数据类型是否正确
import inspect
from inspect import Parameter
from functools import update_wrapper,wraps
def check(fn):
    print('~~~~~~~~~~~~')
    @wraps(fn) #等价于 update_wrapper(wrapper,fn)  ->fn替换wrapper的名字和内容属性等。
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn) #获取签名，同时原始add传入，也就是@check底下的函数
        print(sig)
        params = sig.parameters  #有序字典
        print(params)

        values = list(params.values())  #values = [x:str，y:int]
        for i, x in enumerate(args):   #4,5 列表 调用add函数
            param: Parameter = values[i]

            if param.annotation != param.empty and isinstance(x,param.annotation):
                #param.annotation是一个类型
                print(x, 'ok')
            else:
                print(x, 'not')

        for k ,v in kwargs.items(): #字典 调用add函数
            param:Parameter = params[k]
            if param.annotation != param.empty and isinstance(v,param.annotation):
                print(v,'ok')
            else:
                print(v,'not')

        ret = fn(*args,**kwargs)
        return ret
    print(id(wrapper),'=======')  #wrapper被add替换，被a替换，但并不存在重复替换
    #因为每次被替换的它都是不同的，因为作为check里面的二层函数，每次被调用都是不同的wrapper
    #可以观察id得出这个结论
    return wrapper

@check #add = check(add)
def add(x, y:int) -> int: #注解在冒号后
    return x + y

@check
def a():
    pass

#annotation是注解

#add(x=4, y=5)