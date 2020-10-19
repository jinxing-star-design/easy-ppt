class Temperature:

    def __init__(self, t, unit='c'):
        self._c = None
        self._f = None
        self._k = None

        if unit.lower() == 'k':
            self._k = t
            self._c = self.k2c(t)
        if unit.lower() == 'f':
            self._f = t
            self._c = self.f2c(t)
        else:
            self._c = t

    @property
    def c(self):
        return self._c

    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @property
    def k(self):
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    @classmethod
    def c2f(cls, c1):
        return 9 * c1 / 5 + 32

    @classmethod
    def f2c(cls, f1):
        return (f1 - 32) * 5 / 9

    @classmethod
    def c2k(cls, c1):
        return c1 + 273.15

    @classmethod
    def k2c(cls, k1):
        return k1 - 273.15

    @classmethod
    def f2k(cls, f1):
        return cls.c2k(cls.f2c(f1))

    @classmethod
    def k2f(cls, k1):
        return cls.c2f(cls.k2f(k1))


print(Temperature.c2f(40))
#print(Temperature.f2k(Temperature, 300))

t = Temperature(37)
print(t.c, t.k, t.f)


