# -*- coding: utf-8 -*-
"""
空对象模式
"""
from abc import ABCMeta, abstractmethod


class AbstractCustomer(metaclass=ABCMeta):
    name = ""

    @abstractmethod
    def is_nil(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class RealCustomer(AbstractCustomer):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_nil(self):
        return False


class NullCustomer(AbstractCustomer):

    def get_name(self):
        return "Not Available in Customer Database"

    def is_nil(self):
        return True


class CustomerFactory:

    names = ["Rob", "Joe", "Julie"]

    @classmethod
    def get_customer(cls, name):
        if name in cls.names:
            return RealCustomer(name)
        return NullCustomer()


if __name__ == "__main__":
    customer1 = CustomerFactory.get_customer("Rob")
    customer2 = CustomerFactory.get_customer("Bob")
    customer3 = CustomerFactory.get_customer("Julie")
    customer4 = CustomerFactory.get_customer("Laura")

    print("Customers:")
    print(f"{customer1.get_name()}")
    print(f"{customer2.get_name()}")
    print(f"{customer3.get_name()}")
    print(f"{customer4.get_name()}")
