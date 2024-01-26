# -*- coding: utf-8 -*-
"""
代理模式

结构型模式

- https://www.runoob.com/design-pattern/proxy-pattern.html
"""
from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):

    def __init__(self, file_name):
        self.file_name = file_name
        self.load_from_disk(self.file_name)

    def display(self):
        print(f"Displaying {self.file_name}")

    def load_from_disk(self, file_name):
        print(f"Loading {file_name}")


class ProxyImage(Image):

    def __init__(self, file_name):
        self.file_name = file_name
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.file_name)
        self.real_image.display()


if __name__ == '__main__':
    image = ProxyImage("test_10mb.jpg")
    image.display()
