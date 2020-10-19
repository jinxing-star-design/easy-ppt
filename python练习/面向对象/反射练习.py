class Dispatcher:
    def __init__(self):
        pass

    def reg(self, cmd, fn):
        setattr(self, cmd, fn)  #给自己cmd的这个对象关联一个名为fn的函数

    def run(self):
        while True:
            cmd = input('>>>')
            if cmd == 'quit':
                break
            getattr(self, cmd, lambda self:print('Unknow cmd{}'.format(cmd)))()


def add():
    print('add')


dis = Dispatcher()
dis.reg('a', add)

dis.run()
