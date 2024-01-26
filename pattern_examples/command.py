# -*- coding: utf-8 -*-
"""
命令模式

行为型模式

主要解决：在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系，但某些场合，比如需要对行为进行记录、撤销或重做、事务等处理时，这种无法抵御变化的紧耦合的设计就不太合适。
何时使用：在某些场合，比如要对行为进行"记录、撤销/重做、事务"等处理，这种无法抵御变化的紧耦合是不合适的。在这种情况下，如何将"行为请求者"与"行为实现者"解耦？将一组行为抽象为对象，可以实现二者之间的松耦合。
如何解决：通过调用者调用接受者执行命令，顺序：调用者→接受者→命令。
"""
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class Stock:

    _name = "ABC"
    _quantity = 10

    def buy(self):
        print(f"Stock [Name: {self._name}, Quantity: {self._quantity}] bought.")

    def sell(self):
        print(f"Stock [Name: {self._name}, Quantity: {self._quantity}] sold.")


class BuyStock(Order):

    def __init__(self, stock):
        self._stock = stock

    def execute(self):
        self._stock.buy()


class SellStock(Order):

    def __init__(self, stock):
        self._stock = stock

    def execute(self):
        self._stock.sell()


class Broker:

    _order_list = []

    def take_order(self, order):
        self._order_list.append(order)

    def place_order(self):
        for _order in self._order_list:
            _order.execute()

        self._order_list.clear()


if __name__ == "__main__":
    stock = Stock()
    buy_stock_order = BuyStock(stock)
    sell_stock_order = SellStock(stock)

    broker = Broker()
    broker.take_order(buy_stock_order)
    broker.take_order(sell_stock_order)

    broker.place_order()
