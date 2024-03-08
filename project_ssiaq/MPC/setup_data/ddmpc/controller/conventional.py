""" conventional.py: Contains the abstract 'Controller' super class and conventional controllers. """


from ddmpc.modeling import *
import pandas as pd
from abc import ABC, abstractmethod
import ddmpc.utils.logging as logging


class Controller(ABC):
    """ super class to every controller """

    def __init__(self, step_size: int):
        self.step_size = step_size

    @abstractmethod
    def __call__(self, history: pd.DataFrame) -> tuple[dict, dict]:
        """
        This function is called during the simulation to retrieve the control action.
        :param history: DataFrame with the current state of the system.
        :return: Dictionary with the control action.
        """
        pass


class PID(Controller):
    """ conventional PID controller """

    def __init__(
            self,
            y:              Controlled,
            u:              Control,
            step_size:      int,
            Kp:             float = 0,
            Ti:             float = 0,
            Td:             float = 0,
            reverse_act:    bool = False,
            log_level:      int = logging.NORMAL,
    ):
        """
        :param y: Controlled feature
        :param u: Control feature
        :param dt: Step size. Must be a multiple of the step size of the FMU
        :param Kp: Proportional
        :param Ti: Integral
        :param Td: Differential
        :param reverse_act: Reverse the control action
        """
        super(PID, self).__init__(
            step_size=step_size,
        )

        # control and controlled feature
        self.u = u
        self.y = y

        # PID parameters
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td

        # integrator value
        self.i = 0

        # last error
        self.e_last = 0

        # reverse action
        self.reverse_act = reverse_act

        self.logger: logging.Logger = logging.Logger(prefix=str(self), level=log_level)

    def __str__(self):
        return f'{self.__class__.__name__} - {self.y} controlled by {self.u}'

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def __call__(self, df: pd.DataFrame = None) -> tuple[dict, dict]:
        """
        This function is called during the simulation of the FMU.
        It returns a dict with the control actions.
        """

        self.logger(message=f'y={self.y.value.__round__(2)}, '
                            f'target={self.y.target.__round__(2)} '
                            f'e={self.y.error.__round__(2)}', level=logging.DEBUG)

        # empty control dict
        control_dict = dict()

        # set default value
        control_dict[self.u.variable.col_name] = self.u.default

        # control difference depending on control direction
        e = self.y.error

        # reverse action if reverse_act is true
        if self.reverse_act:
            e = -e

        # Integral
        if self.Ti > 0:
            self.i += 1 / self.Ti * e * self.step_size

        else:
            self.i = 0

        # Differential
        if self.step_size > 0 and self.Td:
            de = self.Td * (e - self.e_last) / self.step_size
        else:
            de = 0

        # PID output
        output = self.Kp * (e + self.i + de)

        # update e_last
        self.e_last = e

        # Limiter
        if output < self.u.lb:
            output = self.u.lb
        elif output > self.u.ub:
            output = self.u.ub

        # Anti wind up
        self.i = output / self.Kp - e

        control_dict[self.u.variable.col_name] = output

        self.logger(message=f'output={output}, i={self.i}', level=logging.DEBUG)

        return control_dict, {}

    def reset(self):
        self.i = 0
        e = self.y.error
        self.e_last = e
