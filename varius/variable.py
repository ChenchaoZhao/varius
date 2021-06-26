import numbers


class Variable(numbers.Real):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        raise RuntimeError("Variable name is immutable.")

    def __add__(self, other):
        pass
