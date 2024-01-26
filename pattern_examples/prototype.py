# -*- coding: utf-8 -*-
"""
原型模式

用于创建重复对象，属于创建型模式。
这种模式实现了一个原型接口，用于创建当前对象的克隆。
实际项目中，原型模式一般和工厂方法模式一起出现，通过clone方法创建对象，然后又工厂方法提供给调用者。

注意：拷贝分为浅拷贝和深拷贝

- https://www.runoob.com/design-pattern/prototype-pattern.html
"""
import copy
from abc import ABCMeta, abstractmethod

# python 使用 copy包实现深拷贝(copy.deepcopy())和浅拷贝（copy.copy())


class Shape(metaclass=ABCMeta):
    _id = ""
    _type = ""

    def __init__(self, id):
        self._id = id

    @abstractmethod
    def draw(self):
        pass

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Shape):
    _type = "Rectangle"

    def draw(self):
        print("Inside Rectangle.draw() method")


class Square(Shape):
    _type = "Square"

    def draw(self):
        print("Inside Square.draw() method")


class Circle(Shape):
    _type = "Circle"

    def draw(self):
        print("Inside Circle.draw() method")


class ShapeCache:
    shape_map = {}

    def get_shape(self, shape_id):
        cached_shape = self.shape_map[shape_id]
        return cached_shape.clone()

    @staticmethod
    def load_cache():
        circle = Circle("1")
        ShapeCache.shape_map[circle.get_id()] = circle

        square = Square("2")
        ShapeCache.shape_map[square.get_id()] = square

        rectangle = Rectangle("3")
        ShapeCache.shape_map[rectangle.get_id()] = rectangle


if __name__ == "__main__":
    ShapeCache.load_cache()
    my_shape = ShapeCache()

    clone_shape = my_shape.get_shape("1")
    print(f"Shape: {clone_shape.get_type()}")
    clone_shape.draw()

    clone_shape = my_shape.get_shape("2")
    print(f"Shape: {clone_shape.get_type()}")
    clone_shape.draw()

    clone_shape = my_shape.get_shape("3")
    print(f"Shape: {clone_shape.get_type()}")
    clone_shape.draw()
