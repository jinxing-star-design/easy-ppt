import inspect

class TypeCheck:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.data = {}

    def __get__(self, instance, owner):
        if instance is not None:
            print(self.__dict__)
            print(self.data[self.name])
            return self.data[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError('')
        self.data[self.name] = value


def typeassert(cls):
    params = inspect.signature(cls).parameters
    print(params,'++++++++++++++++++++')
    for nam, param in params.items():
        print(nam, param)
        if param.annotation != param.empty: #annotation是类型
            setattr(cls, nam, TypeCheck(nam, param.annotation)) #为cls这个类设置一个nam属性(name或者age),

    print(cls)
    return cls


@typeassert #Person = typeassert(Person)
class Person:

    # name = TypeCheck('name', str)
    # age = TypeCheck('age', int)
    # age:int
    # name:str
    def __init__(self, age:int, name:str):
        self.age = age
        self.name = name
        #print(self.age, '----------------------------')
 #print(Person.__dir__(),'=================================')

p1 = Person(19,'tom')
print(p1.__dict__) #p1里面是空的，都被拦截了存储在self.data里
print(p1.name, p1.age)
print(Person.name)