class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return "<Point {}:{}>".format(self.x, self.y)


p = Point(4, 5)
print(p)
print(p())


class Adder:
    def __call__(self, *args, **kwargs):
        ret = 0
        for x in args:
            ret += x
        self.ret = ret


adder = Adder()
print(adder(4, 5, 6))
print(adder.ret)