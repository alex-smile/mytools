# -*- coding: utf-8 -*-
"""
建造者模式

创建型模式

使用多个简单的对象一步一步建成一个复杂的对象。
意图：将一个复杂对象的构建与其表示相分离，使得同样的构建过程可以创建不同的表示。
如何解决：将变与不变分离开。
关键代码：建造者：创建和提供实例，导演：管理建造出来的实例的依赖关系。

- https://www.runoob.com/design-pattern/builder-pattern.html
"""
from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_packing(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Packing(metaclass=ABCMeta):

    @abstractmethod
    def pack(self):
        pass


class Wrapper(Packing):

    def pack(self):
        return "Wrapper"


class Bottle(Packing):

    def pack(self):
        return "Bottle"


class Burger(Item):

    def get_packing(self):
        return Wrapper()


class ColdDrink(Item):

    def get_packing(self):
        return Bottle()


class VegBurger(Burger):

    def get_name(self):
        return "Veg Burger"

    def get_price(self):
        return 25.0


class ChickenBurger(Burger):

    def get_name(self):
        return "Chicken Burger"

    def get_price(self):
        return 50.5


class Pepsi(ColdDrink):

    def get_name(self):
        return "Pepsi"

    def get_price(self):
        return 35.0


class Coke(ColdDrink):

    def get_name(self):
        return "Coke"

    def get_price(self):
        return 30.0


class Meal:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_cost(self):
        return sum(
            item.get_price()
            for item in self._items
        )

    def show_items(self):
        for item in self._items:
            print(f"Item: {item.get_name()}, Packing: {item.get_packing().pack()}, Price: {item.get_price()}")


class MealBuilder:
    def prepare_veg_meal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal

    def prepare_non_veg_meal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal


if __name__ == "__main__":
    builder = MealBuilder()
    meal = builder.prepare_veg_meal()
    print("Veg Meal")
    meal.show_items()
    print(f"TotalCost: {meal.get_cost()}")

    print()
    print()

    meal = builder.prepare_non_veg_meal()
    print("Non-Veg Meal")
    meal.show_items()
    print(f"Total Cost: {meal.get_cost()}")
