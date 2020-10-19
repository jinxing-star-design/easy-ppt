class Animal:
    age = 5

    def __init__(self, name):
        self.name = name

    def shout(self):
        print('{} shouts'.format(type(self).__name__))


class Cat(Animal):
    pass


class Dog(Animal):
    def __init__(self):
        self.age = 20


a = Animal('monster')
a.shout()
print(a.name, a.age)

d = Dog()
print(d.age)


