# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Any


class AbstractHandler(metaclass=ABCMeta):
    next_handler = None

    def set_next(self, _next):
        self.next_handler = _next

    def handle(self, alarms: list) -> None:
        handled_alarms = self.process_alarms(alarms)
        if not handled_alarms:
            return

        if not self.next_handler:
            return

        return self.next_handler.handle(handled_alarms)

    @abstractmethod
    def process_alarms(self, alarms: list) -> list:
        pass


class HandlerA(AbstractHandler):
    def process_alarms(self, alarms: list) -> list:
        print(f"HandlerA process alarms: {alarms}")
        return alarms[:2]


class HandlerB(AbstractHandler):
    def process_alarms(self, alarms: list) -> list:
        print(f"HandlerB process alarms: {alarms}")
        return alarms[:1]


class HandlerC(AbstractHandler):
    def process_alarms(self, alarms: list) -> list:
        print(f"HandlerC process alarms: {alarms}")
        return alarms[:0]


class ChainMixin:
    def chain(self, handlers: list) -> Any:
        handler = None
        for h in reversed(handlers):
            if not h:
                continue
            h.set_next(handler)
            handler = h

        return handler


class HandlerChain(ChainMixin):
    def get_chain_of_handlers(self):
        a = HandlerA()
        b = HandlerB()
        c = HandlerC()

        a.set_next(b)
        b.set_next(c)

        return a

    def get_chain_of_handlers2(self):
        handlers = [
            HandlerA(),
            HandlerB(),
            HandlerC(),
        ]
        return self.chain(handlers)


if __name__ == '__main__':
    handler = HandlerChain().get_chain_of_handlers()
    handler.handle([{"a": 1}, {"b": 2}, {"c": 3}])

    handler2 = HandlerChain().get_chain_of_handlers2()
    handler2.handle([{"a": 1}, {"b": 2}, {"c": 3}])
