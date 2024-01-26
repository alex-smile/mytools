# -*- coding: utf-8 -*-
"""
抽象工厂模式

创建型模式

- https://www.runoob.com/design-pattern/abstract-factory-pattern.html
"""


class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Rectangle draw")


class Square(Shape):
    def draw(self):
        print("Square draw")


class Circle(Shape):
    def draw(self):
        print("Circle draw")


class Color:
    def fill(self):
        pass


class Red(Color):
    def fill(self):
        print("Red fill")


class Green(Color):
    def fill(self):
        print("Green fill")


class Blue(Color):
    def fill(self):
        print("Blue fill")


class AbstractFactory:
    def get_color(self, color):
        pass

    def get_shape(self, shape):
        pass


class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_type):
        if shape_type is None:
            return None
        elif shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        elif shape_type == "SQUARE":
            return Square()
        return None

    def get_color(self, color):
        return None


class ColorFactory(AbstractFactory):
    def get_shape(self, shape_type):
        return None

    def get_color(self, color):
        if color is None:
            return None
        elif color == "RED":
            return Red()
        elif color == "GREEN":
            return Green()
        elif color == "BLUE":
            return Blue()
        return None


class FactoryProducer:
    def get_factory(self, choice):
        if choice == "SHAPE":
            return ShapeFactory()
        elif choice == "COLOR":
            return ColorFactory()
        return None


if __name__ == "__main__":
    shape_factory = FactoryProducer().get_factory("SHAPE")
    circle = shape_factory.get_shape("CIRCLE")
    circle.draw()

    color_factory = FactoryProducer().get_factory("COLOR")
    red = color_factory.get_color("RED")
    red.fill()
