# -*- coding: utf-8 -*-
"""
外观模式

隐藏系统的复杂性，向客户端提供了一个客户端可以访问系统的接口。提供了客户端请求的简化方法和对现有系统类方法的委托调用。
结构型模式。

- https://www.runoob.com/design-pattern/facade-pattern.html
"""


class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Rectangle draw()")


class Square(Shape):
    def draw(self):
        print("Square draw()")


class Circle(Shape):
    def draw(self):
        print("Circle draw()")


class ShapeMaker:

    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()

    def draw_circle(self):
        return self.circle.draw()

    def draw_rectangle(self):
        return self.rectangle.draw()

    def draw_square(self):
        return self.square.draw()

    def draw_bird(self):
        self.circle.draw()
        self.square.draw()


if __name__ == "__main__":
    shape_maker = ShapeMaker()
    shape_maker.draw_circle()
    shape_maker.draw_rectangle()
    shape_maker.draw_square()
    shape_maker.draw_bird()
