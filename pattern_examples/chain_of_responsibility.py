# -*- coding: utf-8 -*-
"""
职责链模式

行为型模式

这种模式给予请求的类型，对请求的发送者和接收者进行解耦。
在这种模式中，通常每个接收者都包含对另一个接收者的引用。如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，依此类推。
"""
from abc import ABCMeta, abstractmethod
from enum import Enum


class LogLevelEnum(Enum):
    DEBUG = 1
    INFO = 2
    ERROR = 3


class AbstractLogger(metaclass=ABCMeta):

    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger

    def log_message(self, level, message):
        if self.level <= level:
            self.write(message)

        if self.next_logger is not None:
            self.next_logger.log_message(level, message)

    @abstractmethod
    def write(self, message):
        pass


class ConsoleLogger(AbstractLogger):

    def write(self, message):
        print(f"Standard Console::Logger: {message}")


class ErrorLogger(AbstractLogger):

    def write(self, message):
        print(f"Error Console::Logger: {message}")


class FileLogger(AbstractLogger):

    def write(self, message):
        print(f"File::Logger: {message}")


class ChainPattern:

    def get_chain_of_loggers(self):
        file_logger = FileLogger(LogLevelEnum.DEBUG.value)
        console_logger = ConsoleLogger(LogLevelEnum.INFO.value)
        error_logger = ErrorLogger(LogLevelEnum.ERROR.value)

        file_logger.set_next_logger(console_logger)
        console_logger.set_next_logger(error_logger)

        return file_logger


if __name__ == "__main__":
    logger_chain = ChainPattern().get_chain_of_loggers()

    logger_chain.log_message(LogLevelEnum.DEBUG.value, "This is a debug level information.")
    logger_chain.log_message(LogLevelEnum.INFO.value, "This is an information.")
    logger_chain.log_message(LogLevelEnum.ERROR.value, "This is an error information.")
