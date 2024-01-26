# -*- coding: utf-8 -*-
"""
备忘录模式

行为型模式

所谓备忘录模式就是在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，这样可以在以后将对象恢复到原先保存的状态
"""


class Memento:
    _state = ""

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    _state = ""

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_state_to_memento(self):
        return Memento(self._state)

    def set_state_from_memento(self, memento):
        self._state = memento.get_state()


class CareTaker:
    _memento_list = []

    def add(self, memento):
        self._memento_list.append(memento)

    def get(self, index):
        return self._memento_list[index]


if __name__ == "__main__":
    originator = Originator()
    care_taker = CareTaker()

    originator.set_state("State #1")
    originator.set_state("State #2")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #3")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #4")

    print(f"Current State: {originator.get_state()}")
    originator.set_state_from_memento(care_taker.get(0))
    print(f"Current State: {originator.get_state()}")
    originator.set_state_from_memento(care_taker.get(1))
    print(f"Current State: {originator.get_state()}")
