#判断用户输入的数据类型是否正确
import inspect
from inspect import Parameter

def check(fn):

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
    return wrapper

@check #add = check(add)
def add(x:str, y:int) -> int: #注解在冒号后

    return x + y


#annotation是注解

add(x=4, y=5)