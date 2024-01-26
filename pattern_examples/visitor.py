# 访问者模式
# - [设计模式之 Visitor（访问者模式）通俗理解](https://www.huaweicloud.com/articles/f3ef7ebba68f193acfee0cd45c1105af.html)
# - [访问者](https://www.liaoxuefeng.com/wiki/1252599548343744/1281319659110433)
import abc
from typing import Iterator


class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit_string(self, element: str):
        raise NotImplementedError

    @abc.abstractmethod
    def visit_float(self, element: float):
        raise NotImplementedError


class Visitable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor: Visitor):
        raise NotImplementedError


class StringElement(Visitable):
    def __init__(self, value: str):
        self._value = value

    def get_value(self):
        return self._value

    # 定义 accept 的具体内容 这里是很简单的一句调用
    def accept(self, visitor: Visitor):
        visitor.visit_string(self)


class FloatElement(Visitable):
    def __init__(self, value: str):
        self._value = value

    def get_value(self):
        return self._value

    # 定义 accept 的具体内容 这里是很简单的一句调用
    def accept(self, visitor: Visitor):
        visitor.visit_float(self)


class ConcreteVisitor(Visitor):
    # 在本方法中,我们实现了对 Collection 的元素的成功访问
    def visit_collection(self, collection: Iterator):
        for item in collection:
            if isinstance(item, Visitable):
                item.accept(self)

    def visit_string(self, element: Visitable):
        print(f"string value: {element.get_value()}")

    def visit_float(self, element: Visitable):
        print(f"float value: {element.get_value()}")


def main():
    visitor = ConcreteVisitor()
    element = StringElement("I am a String")
    visitor.visit_string(element)

    collection = [
        StringElement("I am a String1"),
        StringElement("I am a String2"),
        FloatElement(12.0),
        StringElement("I am a String3"),
    ]
    visitor.visit_collection(collection)


if __name__ == "__main__":
    main()
