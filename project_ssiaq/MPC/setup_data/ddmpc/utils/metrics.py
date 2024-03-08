from typing import Callable


class Metric:

    def __init__(self, func: Callable):
        self.func: Callable = func

    def __call__(self, value):
        return self.func(value)


class MeanSquaredError(Metric):

    def __init__(self):

        def func(x):

            x2 =  (x * x)

            return x

        super(MeanSquaredError, self).__init__(func=func)

class MeanAbsoluteError:

    def __init__(self):

        pass