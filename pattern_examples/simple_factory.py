# -*- coding: utf-8 -*-
"""
简单工厂模式

创建型模式
"""


class Operation(object):
    def get_result(self, number_a, number_b):
        return 0


class OperationAdd(Operation):
    def get_result(self, number_a, number_b):
        return number_a + number_b


class OperationSubtract(Operation):
    def get_result(self, number_a, number_b):
        return number_a - number_b


class OperationMultiply(Operation):
    def get_result(self, number_a, number_b):
        return number_a * number_b


class OperationDivide(Operation):
    def get_result(self, number_a, number_b):
        if number_b == 0:
            raise Exception('Dividend can not be 0')
        return number_a // number_b


class OperationFactory(object):
    @staticmethod
    def create_operation(operate):
        operations = {
            '+': OperationAdd,
            '-': OperationSubtract,
            '*': OperationMultiply,
            '/': OperationDivide,
        }

        try:
            return operations[operate]()
        except KeyError:
            raise ValueError('Do not support operate=%s' % operate)


def main():
    number_a = 2
    number_b = 1
    print(number_a, '+', number_b, '=', OperationFactory.create_operation('+').get_result(number_a, number_b))
    print(number_a, '-', number_b, '=', OperationFactory.create_operation('-').get_result(number_a, number_b))
    print(number_a, '*', number_b, '=', OperationFactory.create_operation('*').get_result(number_a, number_b))
    print(number_a, '/', number_b, '=', OperationFactory.create_operation('/').get_result(number_a, number_b))


if __name__ == '__main__':
    main()
