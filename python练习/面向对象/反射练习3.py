class Base:
    n = 0


class Point(Base):
    z = 6
    d = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def __getattr__(self, item):
        #return "misssing {}".format(item)
        return self.d[item]

    def __setattr__(self, key, value):
        print(key)
        print(value)
        self.d[key] = value

    def __delattr__(self, item):
        print("can not del {}".format(item))


p1 = Point(4, 5)
print(p1.x)
print(p1.z)
print(p1.n)
print(p1.t)
p1.x = 50
print(p1.x)
print(p1.__dict__)
p1.__dict__['x'] = 60  #自己设置实例的__dict__
print(p1.__dict__)
print(p1.x)
