# -*- coding: utf-8 -*-
"""
组合模式，又叫部分整体模式

结构型模式

将对象组合成树形结构以表示"部分-整体"的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。

它在我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以像处理简单元素一样来处理复杂元素，
从而使得客户程序与复杂元素的内部结构解耦。
"""


class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary
        self.subordinates = list()

    def add(self, employee):
        self.subordinates.append(employee)

    def remove(self, employee):
        self.subordinates.remove(employee)

    def get_subordinates(self):
        # 应返回一份数据拷贝，防止在外部改变列表内容
        return self.subordinates

    def __str__(self):
        return f"Employee: [Name: {self.name}, dept: {self.dept}, salary: {self.salary}]"


if __name__ == "__main__":
    ceo = Employee("John", "CEO", 30000)

    head_sales = Employee("Robert", "Head Sales", 20000)
    head_marketing = Employee("Michel", "Head Marketing", 20000)

    clerk1 = Employee("Laura", "Marketing", 10000)
    clerk2 = Employee("Bob", "Marketing", 10000)

    sales_executive1 = Employee("Richard", "Sales", 10000)
    sales_executive2 = Employee("Rob", "Sales", 10000)

    ceo.add(head_sales)
    ceo.add(head_marketing)

    head_sales.add(sales_executive1)
    head_sales.add(sales_executive2)

    head_marketing.add(clerk1)
    head_marketing.add(clerk2)

    print(f"{ceo}")
    for head_employee in ceo.get_subordinates():
        print(head_employee)
        for employee in head_employee.get_subordinates():
            print(employee)
