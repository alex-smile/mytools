# -*- coding: utf-8 -*-
"""
在面向对象设计中，我们还有一个很重要的设计原则，那就是合成/聚合复用原则。即优先使用对象合成/聚合，而不是类继承[DP]

合成/聚合复用原则（CARP），尽量使用合成/聚合，尽量不要使用类继承。

合成（组合，Composition）：一种强的“拥有”关系，体现严格的部分和整体的关系，部分和整体的生命周期一样，比如：大雁和翅膀是合成关系
聚合（Aggregation）：表示一种弱的“拥有”关系，体现A对象可以包含B对象，但B对象不是A对象的一部分，比如：大雁和雁群是聚合关系

桥接模式

结构型模式

这种模式涉及到一个作为桥接的接口，使得实体类的功能独立于接口实现类。这两种类型的类可被结构化改变而互不影响。

意图：将抽象部分与实现部分分离，使它们都可以独立的变化。它通过提供抽象化和实现化之间的桥接结构，来实现二者的解耦。
主要解决：在有多种可能会变化的情况下，用继承会造成类爆炸问题，扩展起来不灵活。
何时使用：实现系统可能有多个角度分类，每一种角度都可能变化。
如何解决：把这种多角度分类分离出来，让它们独立变化，减少它们之间耦合。
使用场景：一个类存在两个独立变化的维度，且这两个维度都需要进行扩展。
"""
from abc import ABCMeta, abstractmethod


class PhoneSoftware(metaclass=ABCMeta):
    """
    手机软件
    """
    @abstractmethod
    def run(self):
        pass


class PhoneGame(PhoneSoftware):

    def run(self):
        print("运行手机游戏")


class PhoneAddressList(PhoneSoftware):

    def run(self):
        print("运行手机通讯录")


class PhoneBrand(metaclass=ABCMeta):
    """
    手机品牌
    """
    phone_software = None

    def set_software(self, software):
        self.phone_software = software

    @abstractmethod
    def run(self):
        pass


class PhoneBrandM(PhoneBrand):

    def run(self):
        self.phone_software.run()


class PhoneBrandN(PhoneBrand):

    def run(self):
        self.phone_software.run()


if __name__ == "__main__":
    brand = PhoneBrandM()
    brand.set_software(PhoneGame())
    brand.run()
    brand.set_software(PhoneAddressList())

    brand = PhoneBrandN()
    brand.set_software(PhoneGame())
    brand.run()
    brand.set_software(PhoneAddressList())
