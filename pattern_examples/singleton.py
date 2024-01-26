# -*- coding: utf-8 -*-
"""
单例模式

创建型模式
"""
import threading


class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class SingletonMeta2(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        self.__lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is not None:
            return self.__instance

        with self.__lock:
            if self.__instance is not None:
                return self.__instance

            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance


class Singleton2(object):
    def __new__(cls, *args, **kwargs):
        # 此处，不能使用双下划线变量名，因其会导致python解释器重写属性名
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Spam(metaclass=SingletonMeta):
    def __init__(self):
        print('Creating Spam')


class Spam2(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating Spam2")


class Spam3(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating Spam3")


class Spam4(Singleton2):
    def __init__(self):
        print("Creating Spam4")


class Spam5(Singleton2):
    def __init__(self):
        print("Creating Spam5")


if __name__ == "__main__":
    print(Spam.__dict__)

    a = Spam()
    b = Spam()
    c = Spam()
    print(repr(a))
    print(repr(b))
    print(repr(c))
    print(a is b)
    print(a is c)

    e = Spam2()
    f = Spam2()
    print(repr(e))
    print(repr(f))
    print(e is f)
    print(a is not e)

    g = Spam3()
    h = Spam3()
    print(repr(g))
    print(repr(h))
    print(g is h)
    print(a is not g)

    print(Spam4.__dict__)

    i = Spam4()
    j = Spam4()
    k = Spam4()
    print(i.__dict__)
    print(repr(i))
    print(repr(j))
    print(repr(k))
    print(i is j)
    print(i is k)

    m = Spam5()
    n = Spam5()
    print(repr(m))
    print(repr(n))
    print(m is n)
    print(i is not m)
