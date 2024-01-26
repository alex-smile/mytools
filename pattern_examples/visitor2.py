# 访问者模式
# - [访问者](https://www.liaoxuefeng.com/wiki/1252599548343744/1281319659110433)
import abc
import os
from typing import Iterator
import dataclasses


class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def visit_dir(dir_: str):
        raise NotImplementedError

    @abc.abstractclassmethod
    def visit_file(file_: str):
        raise NotImplementedError


@dataclasses.dataclass
class FileStructure:
    path: str

    def handle(self, visitor: Visitor):
        self._scan(self.path, visitor)

    def _scan(self, path: str, visitor: Visitor):
        for current_folder, folders, files in os.walk(path):
            for filename in files:
                visitor.visit_file(os.path.join(current_folder, filename))

            for folder in folders:
                visitor.visit_dir(os.path.join(current_folder, folder))


class PythonFileVisitor(Visitor):
    def visit_dir(self, path: str):
        print(f"visit dir: {path}")

    def visit_file(self, path: str):
        if path.endswith(".py"):
            print(f"found python file: {path}")


def main():
    handler = FileStructure(".")
    handler.handle(PythonFileVisitor())


if __name__ == '__main__':
    main()