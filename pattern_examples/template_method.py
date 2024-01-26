# -*- coding: utf-8 -*-
"""
模板方法模式

抽象类公开的模板方法，定义一个操作中的算法骨架，而将一些步骤延迟到子类中。子类不改变算法的结构即可重定义算法的某些特定步骤。
行为型模式。
"""
from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):

    def initialize(self):
        print(f"{self.get_game_name()} Game Initialized! Start Playing")

    def start_play(self):
        print(f"{self.get_game_name()} Game started. Enjoy the game!")

    def end_play(self):
        print(f"{self.get_game_name()} Game finished!\n")

    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()

    @abstractmethod
    def get_game_name(self):
        pass


class Cricket(Game):
    def get_game_name(self):
        return "Cricket"


class Football(Game):
    def get_game_name(self):
        return "Football"


if __name__ == "__main__":
    game = Cricket()
    game.play()

    game = Football()
    game.play()
