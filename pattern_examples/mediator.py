# -*- coding: utf-8 -*-
"""
中介者模式

行为型模式

意图：用一个中介对象来封装一系列的对象交互，中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。
主要解决：对象与对象之间存在大量的关联关系，这样势必会导致系统的结构变得很复杂，同时若一个对象发生改变，我们也需要跟踪与之相关联的对象，同时做出相应的处理。
何时使用：多个类相互耦合，形成了网状结构。
如何解决：将上述网状结构分离为星型结构。
使用场景： 1、系统中对象之间存在比较复杂的引用关系，导致它们之间的依赖关系结构混乱而且难以复用该对象。 2、想通过一个中间类来封装多个类中的行为，而又不想生成太多的子类。
"""
import datetime


def now_str():
    return datetime.datetime.now().strftime("YYYY-mm-dd HH:MM:SS")


class ChatRoom:

    @staticmethod
    def show_message(user, message):
        print(f"{now_str()} [{user.get_name()}]: {message}")


class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def send_message(self, message):
        ChatRoom.show_message(self, message)


if __name__ == "__main__":
    robert = User("Robert")
    john = User("John")

    robert.send_message("Hi! John!")
    john.send_message("Hello! Robert!")
