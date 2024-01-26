# -*- coding: utf-8 -*-
"""
享元模式

结构型模式

运用共享技术，减少创建对象的数量，以减少内存占用和提高性能。
享元模式尝试重用现有的同类对象，如果未找到匹配的对象，则创建新对象。

何时使用：
    1、系统中有大量对象。
    2、这些对象消耗大量内存。
    3、这些对象的状态大部分可以外部化。
    4、这些对象可以按照内蕴状态分为很多组，当把外蕴对象从对象中剔除出来时，每一组对象都可以用一个对象来代替。
    5、系统不依赖于这些对象身份，这些对象是不可分辨的。
如何解决：用唯一标识码判断，如果在内存中有，则返回这个唯一标识码所标识的对象。
关键代码：用 HashMap 存储这些对象。
使用场景： 1、系统有大量相似对象。 2、需要缓冲池的场景。
注意事项： 1、注意划分外部状态和内部状态，否则可能会引起线程安全问题。 2、这些类必须有一个工厂对象加以控制。
"""
import random
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    color = ""
    x = 0
    y = 0
    radius = 0

    def __init__(self, color):
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_radius(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Circle: Draw() [Color: {self.color}, x: {self.x}, y: {self.y}, radius: {self.radius}]")


class ShapeFactory:

    circle_map = {}

    @classmethod
    def get_circle(cls, color):
        circle = cls.circle_map.get(color)

        if circle is None:
            circle = Circle(color)
            cls.circle_map[color] = circle
            print(f"Creating circle of color: {color}")

        return circle


def get_random():
    return random.randint(1, 100)


if __name__ == "__main__":
    colors = ["Red", "Green", "Blue", "White", "Black"]

    for i in range(20):
        circle = ShapeFactory.get_circle(random.choice(colors))
        circle.set_x(get_random())
        circle.set_y(get_random())
        circle.set_radius(100)
        circle.draw()
