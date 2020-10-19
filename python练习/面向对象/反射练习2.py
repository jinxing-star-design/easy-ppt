class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    def show(self):
        print(self)


p1 = Point(4, 5)
p2 = Point(10, 10)
print(repr(p1), repr(p2), sep='\n')
print(p1.__dict__)
setattr(p1, 'y', 16)   #setattr的用法
setattr(p1, 'z', 10)
print(getattr(p1, '__dict__'))   #getattr的用法

if hasattr(p1, 'show'):
    getattr(p1, 'show')()

#为类增加方法
if not hasattr(Point, 'add'):
    setattr(Point, 'add', lambda self, other: Point(self.x + self.x, self.y + other.y))

print(Point.add)
print(p1.add)
print(p1.add(p2))

#为实例增加方法
if not hasattr(Point, 'sub'):
    setattr(Point, 'sub', lambda self, other: Point(self.x - self.x, self.y- other.y))

print(p1.sub(p2)) #输出实例属性的计算结果
print(p1.sub) #输出实例的属性

#add在谁里面，sub在谁里面
print(p1.__dict__)
print(Point.__dict__)

#，它在运行时改变类或实例的方式反射具有更大的灵活性






