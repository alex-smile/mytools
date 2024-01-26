# -*- coding: utf-8 -*-
"""
装饰模式

结构型模式
"""
import functools


# 装饰器不需要传入参数
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# 相当于 log = log(now)
@log
def now():
    print("2020-03-10")


# 装饰器需要传入参数
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{text} {func.__name__}:")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# 相当于 now = log('execute')(now)
@log2("execute")
def now2():
    print("2020-03-10")


# 带可选参数的装饰器
# 支持 @decorator, @decorator(x, y, z)
def logged(func=None, name=None, message=None):
    if func is None:
        return functools.partial(logged, name=name, message=message)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}, name={name}, message={message}")
        return func(*args, **kwargs)
    return wrapper


@logged
def add(x, y):
    return x + y


@logged(name='example')
def spam():
    print("Spam!")


class Log3:
    def __init__(self, func):
        functools.wraps(func)(self)

    def __call__(self, *args, **kwargs):
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        import types
        return types.MethodType(self, instance)


@Log3
def now3():
    print("2020-03-10")


class Log4:
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"call {func.__name__}")
            return func(*args, **kwargs)
        return wrapper


@Log4()
def now4():
    print("2020-03-10")


# 将装饰器定义为类的一部分
class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# As an instance method
a = A()


@a.decorator1
def spam_a():
    pass


# As a class method
@A.decorator2
def grok_b():
    pass


if __name__ == "__main__":
    now()
    print(now.__name__)

    now2()
    print(now2.__name__)

    now3()
    print(now3.__name__)

    now4()

    add(1, 2)
    spam()

    spam_a()
    grok_b()
