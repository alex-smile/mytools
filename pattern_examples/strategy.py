# -*- coding: utf-8 -*-
"""
策略模式

行为型模式
"""
import math
from abc import ABC, abstractmethod


class CashDiscount(ABC):
    @abstractmethod
    def accept_cash(self, money):
        pass

    @staticmethod
    def create(discount_type):
        if discount_type == "normal":
            return CashNormal()
        elif discount_type == "rebate_0.9":
            return CashRebate(0.9)
        elif discount_type == "rebate_0.8":
            return CashRebate(0.8)
        elif discount_type == "return_300_100":
            return CashReturn(300, 100)
        else:
            raise Exception("Do not support discount_type={discount_type}".format(discount_type=discount_type))


class CashNormal(CashDiscount):
    def accept_cash(self, money):
        return money


class CashRebate(CashDiscount):
    def __init__(self, money_rebate):
        # 折扣，如9折
        self.money_rebate = money_rebate

    def accept_cash(self, money):
        return money * self.money_rebate


class CashReturn(CashDiscount):
    def __init__(self, money_condition, money_return):
        # money_condition为返利条件，如满300，
        # money_return为返利值，如返100
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money < self.money_condition:
            return money
        return money - math.floor(money / self.money_condition) * self.money_return


class Product:
    def __init__(self, price):
        self.price = price


class ProductDealRecord:

    def __init__(self, product, number, discount_type):
        self.cash_discount = CashDiscount.create(discount_type)
        self.product = product
        self.number = number

    def get_result(self):
        return self.cash_discount.accept_cash(self.product.price * self.number)


class Deal:
    product_deal_records = []

    def get_result(self):
        return sum([
            record.get_result()
            for record in self.product_deal_records
        ])

    def add_product_deal_record(self, product_deal_record):
        self.product_deal_records.append(product_deal_record)


if __name__ == "__main__":
    product_a = Product(20)
    product_b = Product(60)

    deal = Deal()

    record = ProductDealRecord(product_a, 10, "rebate_0.9")
    deal.add_product_deal_record(record)

    record = ProductDealRecord(product_b, 20, "return_300_100")
    deal.add_product_deal_record(record)

    cash = deal.get_result()
    print(cash)
