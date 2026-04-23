from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def to_string(self):
        pass


class Payable(ABC):

    @abstractmethod
    def calculate_payment(self):
        pass