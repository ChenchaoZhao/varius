import numbers
from typing import *

from . import _CURRENT_VERSION as CV
from . import VARIABLE_STORAGE as VS


class Variable(numbers.Real):
    def __init__(self, name: str, value: Optional[Union[float, int]] = None):
        self.__name = name
        if CV is not None and value is not None:
            VS[CV][name] = value

    @property
    def value(self) -> Union[float, int]:
        if CV is not None:
            return self.__getitem__(CV)
        else:
            raise RuntimeError("Current version is `None`.")

    @value.setter
    def value(self, value: Union[float, int]):

        if CV is not None:
            self.__setitem__(CV, value)
        else:
            raise RuntimeError("Current version is `None`.")

    def __call__(self, value: Union[float, int]):
        self.value = value

    def __getitem__(self, version: str) -> Union[float, int]:
        if version in VS:
            if self.name in VS[version]:
                return VS[version][self.name]
            else:
                raise KeyError(
                    f"Variable `{self.name}` was not assigned a value in version `{version}`."
                )
        else:
            raise KeyError(f"Version `{version}` does not exist.")

    def __setitem__(self, version: str, value: Union[float, int]):
        if not isinstance(value, (float, int)):
            raise TypeError(
                f"Assigned value should be float or int but get {type(value)}"
            )
        VS[version][self.name] = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name):
        raise RuntimeError("Variable name is immutable.")

    def __abs__(self):
        pass

    def __add__(self, other):
        pass

    def __ceil__(self):
        pass

    def __eq__(self, other):
        pass

    def __float__(self):
        pass

    def __floor__(self):
        pass

    def __floordiv__(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __pow__(self, other):
        pass

    def __round__(self):
        pass

    def __truediv__(self, other):
        pass

    def __trunc__(self):
        pass

    __radd__ = __add__

    __rfloordiv__ = __floordiv__

    __rmod__ = __mod__

    __rmul__ = __mul__

    __rpow__ = __pow__

    __rtruediv__ = __truediv__
