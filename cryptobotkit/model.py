import attr
from abc import ABC, abstractmethod


@attr.s
class Exchange(ABC):
    """An abstract base class with methods to interact with a crypto exchange"""
    base_url = attr.ib(type=str)



class Strategy(ABC):
    """An abstract base class to execute a trading strategy"""

    @abstractmethod
    def execute():
        pass


@attr.s
class Fund(ABC):
    """An abstract base class to represent an investement fund and its trading strategy"""

    strategy = attr.ib()
