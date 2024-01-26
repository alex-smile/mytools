# -*- coding: utf-8 -*-
"""
状态模式
状态模式与策略模式很类似，将类的”状态”封装了起来，在执行动作时进行自动的转换，从而实现，类在不同状态下同一动作显示不同结果。
它与策略模式的区别在于，这种转换是”自动”，“无意识”的。
策略模式会控制对象使用什么策略，而状态模式会自动改变状态。

行为型模式

案例：糖果机，4个动作，4个状态，动作会导致状态的变化
使用“状态模式”，糖果机根本不需要清楚状态的改变，它只用调用状态的方法就行。状态的改变是在状态内部发生的。

https://www.runoob.com/w3cnote/state-vs-strategy.html
"""
from abc import ABC, abstractmethod
from enum import Enum


class StateEnum(Enum):
    # 没有硬币
    NO_QUARTER = "no_quarter"
    # 投币
    HAS_QUARTER = "has_quarter"
    # 出售糖果
    SOLD = "sold"
    # 糖果售尽
    SOLD_OUT = "sold_out"


class State(ABC):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    @abstractmethod
    def insert_quarter(self):
        """投币"""
        pass

    @abstractmethod
    def eject_quarter(self):
        """退币"""
        pass

    @abstractmethod
    def turn_crank(self):
        """转动出糖曲轴"""
        pass

    @abstractmethod
    def dispense(self):
        """发糖"""
        pass

    def _return_quarter(self):
        """退还硬币"""
        print("退币...")


class NoQuarterState(State):

    def insert_quarter(self):
        print("你投入了一个硬币")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print("没有硬币，无法弹出")

    def turn_crank(self):
        print("请先投币")

    def dispense(self):
        print("没有投币，无法发放糖果")


class HasQuarterState(State):

    def insert_quarter(self):
        print("请不要重复投币！")
        self._return_quarter()

    def eject_quarter(self):
        self._return_quarter()
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("转动曲轴，准备发糖")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def dispense(self):
        print("this method don't support")


class SoldState(State):

    def insert_quarter(self):
        print("已投币，请等待糖果")
        self._return_quarter()

    def eject_quarter(self):
        print("无法退币，正在发放糖果，请等待")

    def turn_crank(self):
        print("已按过曲轴，请等待")

    def dispense(self):
        candy_count = self.gumball_machine.get_candy_count()
        if candy_count > 0:
            print("分发一颗糖果")
            self.gumball_machine.set_candy_count(candy_count - 1)
            if candy_count > 0:
                self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
                return

        print("抱歉，糖果已售尽")
        self.gumball_machine.set_state(self.gumball_machine.sold_out_state)


class SoldOutState(State):

    def insert_quarter(self):
        print("糖果已经售尽")

    def eject_quarter(self):
        print("没有投币，无法退币")

    def turn_crank(self):
        print("糖果已经售尽")

    def dispense(self):
        print("糖果已经售尽")


class GumballMachine(State):

    def __init__(self, count=0):
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.sold_out_state = SoldOutState(self)

        self.candy_count = count
        self.state = self.sold_out_state
        if self.candy_count > 0:
            self.state = self.no_quarter_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()

    def dispense(self):
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def set_candy_count(self, candy_count):
        self.candy_count = candy_count

    def get_candy_count(self):
        return self.candy_count


if __name__ == "__main__":
    gumball_machine = GumballMachine(5)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.dispense()
