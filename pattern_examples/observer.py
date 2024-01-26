# -*- coding: utf-8 -*-
"""
观察者模式

行为型模式

一个对象（目标对象）的状态发生改变，所有的依赖对象（观察者对象）都将得到通知，进行广播通知。

https://www.runoob.com/design-pattern/observer-pattern.html
"""
from abc import ABCMeta, abstractmethod


class Subject:

    def __init__(self, state=0):
        self.observers = list()
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        self.notifyAllObservers()

    def attach(self, observer):
        self.observers.append(observer)

    def notifyAllObservers(self):
        for observer in self.observers:
            observer.update()


class Observer(metaclass=ABCMeta):

    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    @abstractmethod
    def update(self):
        pass


class BinaryObserver(Observer):

    def update(self):
        print(f"Binary String: {self.subject.getState()}")


class OctalObserver(Observer):

    def update(self):
        print(f"Octal String: {self.subject.getState()}")


class HexObserver(Observer):

    def update(self):
        print(f"Hex String: {self.subject.getState()}")


if __name__ == "__main__":
    subject = Subject(state=0)

    HexObserver(subject)
    OctalObserver(subject)
    BinaryObserver(subject)

    print("First state change: 15")
    subject.setState(15)
    print("Second state change: 10")
    subject.setState(10)
