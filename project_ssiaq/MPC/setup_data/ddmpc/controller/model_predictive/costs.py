from abc import ABC, abstractmethod
from casadi import MX
from typing import Union


class Cost(ABC):
    """ cost function for objective """

    def __init__(
            self,
            weight: float,
    ):
        """ scalar weight for the cost function """

        self.weight = weight

    def __str__(self):
        return f'CostOrder({self.__class__.__name__})'

    def __repr__(self):
        return f'CostOrder({self.__class__.__name__})'

    @abstractmethod
    def __call__(self, mx: Union[MX, float]) -> Union[MX, float]:
        """ the call function takes a casadi MX variable and applies the cost function to it """
        pass


class Linear(Cost):
    """ linear cost function """

    def __init__(
            self,
            weight: float = 1,
            offset: float = 0,
            norm:   float = 1,
    ):
        super(Linear, self).__init__(
            weight=weight,
        )

        # the offset can be used to shift the costs by a constant factor
        self.offset = offset
        self.norm = norm

    def __call__(self, mx: Union[MX, float]) -> Union[MX, float]:
        """ the call function takes a casadi MX variable and applies the cost function to it """

        return (mx - self.offset) / self.norm * self.weight


class AbsoluteLinear(Cost):
    """ absolute linear cost function """

    def __init__(
            self,
            weight: float = 1.0,
            norm: float = 1.0,
    ):
        super(AbsoluteLinear, self).__init__(
            weight=weight,
        )
        self.norm = norm

    def __call__(self, mx: Union[MX, float]) -> Union[MX, float]:
        """ the call function takes a casadi MX variable and applies the cost function to it """

        return (mx / self.norm) * self.weight


class Quadratic(Cost):

    def __init__(
            self,
            weight: float = 1,
            norm: float = 1,
            offset: float = 0,
    ):

        super(Quadratic, self).__init__(
            weight=weight,
        )

        # before squaring the feature is divided by the norm
        self.norm = norm
        self.offset = offset

    def __call__(self, mx: Union[MX, float]) -> Union[MX, float]:
        """ the call function takes a casadi MX variable and applies the cost function to it """

        return ((mx - self.offset) / self.norm) ** 2 * self.weight
