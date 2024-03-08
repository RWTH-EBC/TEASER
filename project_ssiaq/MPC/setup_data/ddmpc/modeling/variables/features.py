from abc import ABC, abstractmethod
from typing import Union, Callable

from typing import Optional
from ddmpc.modeling.variables.main import *
from ddmpc.utils.modes import Mode
import casadi as ca


class Feature(ABC):

    all: list['Feature'] = list()

    def __init__(
            self,
            variable:   Variable,
    ):

        self.variable:  Variable = variable

        self.all.append(self)

    def __str__(self):
        return f'{self.__class__.__name__}({self.variable})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.variable})'

    def __eq__(self, other):

        assert isinstance(other, Feature) or isinstance(other, Variable)

        return hash(self) == hash(other)

    def __ne__(self, other):
        """ returns True if the name of the Feature is not equal to the name of the other Feature """

        return not self.__eq__(other)

    def __hash__(self):
        """ returns the hash based on the name of the Source """

        return hash(self.variable)

    def update(self, df: pd.DataFrame, idx: int, inplace: bool = True) -> pd.DataFrame:

        if not inplace:
            df = df.copy(deep=True)

        df = self.variable.update(df=df, idx=idx)
        df = self._update(df=df, idx=idx)

        return df

    def process(self, df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:

        if not inplace:
            df = df.copy(deep=True)

        df = self.variable.process(df=df)
        df = self._process(df=df)

        return df

    @abstractmethod
    def _update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:
        pass

    @abstractmethod
    def _process(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def __sub__(self, other):
        return Connection(Subtraction(b1=self, b2=other))

    def __mul__(self, other):
        return Connection(Multiplication(b1=self, b2=other))

    def __add__(self, other):
        return Connection(Addition(b1=self, b2=other))


class Controlled(Feature):

    def __init__(
            self,
            variable: Variable,
            mode:   Mode,
    ):

        Feature.__init__(
            self,
            variable=variable,
        )

        self.mode: Mode = mode

        # running variables
        self.time:              Optional[float] = None
        self.value:             Optional[float] = None
        self.error:             Optional[float] = None
        self.target:            Optional[float] = None
        self.lb:                Optional[float] = None
        self.ub:                Optional[float] = None

        # column names
        self.col_name_error:    str = f'Error({self.variable.name})'
        self.col_name_lb:       str = f'LowerBound({self.variable.name})'
        self.col_name_ub:       str = f'UpperBound({self.variable.name})'
        self.col_name_target:   str = f'Target({self.variable.name})'
        self.col_name_mode:     str = f'Mode({self.variable.name})'

    def _update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        self.time = int(df.loc[row, 'SimTime'])
        self.value = float(df.loc[row, self.variable.col_name])

        self.error = float(self.mode.error(value=self.value, time=self.time))
        self.target = float(self.mode.target(time=self.time))
        self.lb, self.ub = self.mode.bounds(time=self.time)

        # write to DataFrame
        df.loc[row, self.col_name_error] = self.error
        df.loc[row, self.col_name_target] = self.target
        df.loc[row, self.col_name_lb] = self.lb
        df.loc[row, self.col_name_ub] = self.ub
        df.loc[row, self.col_name_mode] = self.mode

        return df

    def _process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name_lb] = df['SimTime'].apply(lambda t: self.mode.lb(t))
        df[self.col_name_ub] = df['SimTime'].apply(lambda t: self.mode.ub(t))
        df[self.col_name_target] = df['SimTime'].apply(lambda t: self.mode.target(t))

        try:
            if self.col_name_error not in df.columns:

                if df[self.col_name_target].isna().all():

                    df[self.col_name_error] = df[
                        [self.variable.col_name, self.col_name_lb, self.col_name_ub]
                    ].apply(lambda x: max(min(x[0] - x[1], 0), max(x[0] - x[2], 0), key=abs), axis=1)

                else:

                    df[self.col_name_error] = df[self.col_name_target] - df[self.variable.col_name]
        except:
            pass

        return df


class Control(Feature):

    def __init__(
            self,
            variable:     Variable,
            lb:         float,
            ub:         float,
            default:    float,
            cutoff:     float = None,
    ):

        Feature.__init__(
            self,
            variable=variable,
        )

        self.lb:        float = lb
        self.ub:        float = ub
        self.default:   float = default
        self.cutoff:    float = cutoff

    def _update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:
        return df

    def _process(self, df: pd.DataFrame) -> pd.DataFrame:
        return df


class Disturbance(Feature):

    def __init__(
            self,
            variable:         Variable,
            forecast_name:  str = None,
    ):
        Feature.__init__(
            self,
            variable=variable,
        )

        self.forecast_name: str = forecast_name

    def _update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:
        return df

    def _process(self, df: pd.DataFrame) -> pd.DataFrame:
        return df


class Connection(Feature):

    def __init__(
            self,
            variable: Constructed,
    ):

        assert isinstance(variable, Constructed), 'The Variables for Connections can only be of type Constructed!'

        Feature.__init__(
            self,
            variable=variable,
        )

    def _update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:
        return df

    def _process(self, df: pd.DataFrame) -> pd.DataFrame:
        return df


class Tracking(Feature):

    def _update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:
        return df

    def _process(self, df: pd.DataFrame) -> pd.DataFrame:
        return df


""" Constructed Features """


class Change(Constructed):
    """ used to calculate the change between to time steps """

    def __init__(
            self,
            base: Union[Variable, Feature],
            plt_opts: Union[PlotOptions, None] = None,
    ):

        if isinstance(base, Feature):
            base = base.variable

        if plt_opts is None:
            plt_opts = base.plt_opts

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({base.name})',
            plt_opts=plt_opts,
        )

        self.base = base

    @property
    def subs(self) -> list[Variable]:
        return [self.base]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        if idx <= 1:
            return df

        row = df.index[idx]
        previous_row = df.index[idx-1]

        df.loc[row, self.col_name] = float(df.loc[row, self.base.col_name] -
                                           df.loc[previous_row, self.base.col_name])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        if self.base.col_name not in df.columns:
            df = self.base.process(df)

        df[self.col_name] = df[self.base.col_name] - df[self.base.col_name].shift(1)

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k not in self.base.mx:
            print(k, 'not in', self.base.mx.keys(), 'base:', self.base)
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.base} which is base for {self}.')

        if (k - 1) not in self.base.mx:
            raise ValueError(f'Did not find k={k}-1={k-1} in the keys of mx for {self.base} which is base for {self}.')

        lhs = self[k]
        rhs = self.base[k] - self.base[k-1]

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 1


class Average(Constructed):

    """ used to calculate the average of multiple Sources """

    def __init__(
            self,
            name:       str,
            bases:      list[Union[Variable, Feature]],
            plt_opts:   PlotOptions,
    ):

        self.sources: list[Variable] = list()
        for base in bases:
            if isinstance(base, Feature):
                self.sources.append(base.variable)
            elif isinstance(base, Variable):
                self.sources.append(base)
            else:
                raise ValueError('Please only pass a list of Sources for Features!')

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({name})',
            plt_opts=plt_opts,
        )

    @property
    def n(self):
        return len(self.sources)

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]
        df.loc[row, self.col_name] = sum(df.loc[row, source.col_name] for source in self.sources) / self.n

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        try:
            df[self.col_name] = sum(df[source.col_name] for source in self.sources) / self.n

        except TypeError as e:

            print('col_names:', [source.col_name for source in self.sources])
            print('col_names:', [df[source.col_name] for source in self.sources])
            print('self.n:', self.n)

            raise e

        return df

    @property
    def subs(self) -> list[Variable]:
        return self.sources

    def constraint(self, k: int) -> ca.MX:

        for s in self.sources:
            assert k in s.mx

        lhs = self[k]

        rhs = ca.sum1(ca.vertcat(*[source[k] for source in self.sources])) / ca.DM(self.n)

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class RunningMean(Constructed):

    def __init__(
            self,
            base:       Union[Variable, Feature],
            n:          int,
            plt_opts:   Union[PlotOptions, None] = None,
    ):

        if isinstance(base, Feature):
            base = base.variable

        if plt_opts is None:
            plt_opts = PlotOptions(line=fmt.line_dotted, color=fmt.grey)

        Constructed.__init__(
            self,
            name=f'RunningMean({base}, n={n})',
            plt_opts=plt_opts,
        )

        self.source:    Variable = base
        self.plt_opts:  PlotOptions = plt_opts
        self.n:         int = n

    @property
    def subs(self) -> list[Variable]:
        return [self.source]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        if idx <= self.n:
            return df

        df.loc[df.index[idx], self.col_name] = sum(
            [df.loc[df.index[idx - i], self.source.col_name] for i in range(0, self.n)]
        ) / self.n

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df[self.source.col_name].rolling(self.n).mean()

        return df

    def constraint(self, k: int) -> ca.MX:

        assert k in self.mx
        for i in range(0, self.n):
            assert k - i in self.source.mx

        lhs = self[k]
        rhs = ca.sum1(ca.vertcat(*[self.source[k-i] for i in range(0, self.n)])) / ca.DM(self.n)

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return self.n


class HeatFlow(Constructed):

    def __init__(
            self,
            name:               str,
            mass_flow:          Union[Variable, Feature],
            temperature_in:     Union[Variable, Feature],
            temperature_out:    Union[Variable, Feature],
            cp:                 float = 4.18,
            den:                float = 1000,
            plt_opts:           Union[PlotOptions, None] = None,

    ):

        # plot options
        if plt_opts is None:
            plt_opts = PlotOptions(
                color=fmt.green,
                line=fmt.line_solid,
                label=name,
            )

        # temperatures and mass flow
        if isinstance(mass_flow, Feature):
            mass_flow = mass_flow.variable

        if isinstance(temperature_in, Feature):
            temperature_in = temperature_in.variable

        if isinstance(temperature_out, Feature):
            temperature_out = temperature_out.variable

        self.mass_flow:         Variable = mass_flow
        self.temperature_in:    Variable = temperature_in
        self.temperature_out:   Variable = temperature_out

        # heat capacity and density
        self.cp:                float = cp
        self.den:               float = den

        # super call
        Constructed.__init__(
            self,
            name=name,
            plt_opts=plt_opts,
        )

    @property
    def subs(self) -> list[Variable]:
        return [self.mass_flow, self.temperature_in, self.temperature_out]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = float(
            df.loc[row, self.mass_flow.col_name]
            * (df.loc[row, self.temperature_in.col_name] - df.loc[row, self.temperature_out.col_name])
            * self.cp
            * self.den
        )

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df[self.mass_flow.col_name] * \
                            (df[self.temperature_in.col_name] - df[self.temperature_out.col_name]) \
                            * self.cp \
                            * self.den

        return df

    def constraint(self, k: int) -> ca.MX:

        assert k in self.mx
        assert k in self.mass_flow.mx
        assert k in self.temperature_in.mx
        assert k in self.temperature_out.mx

        lhs = self[k]
        rhs = self.mass_flow[k] * (self.temperature_in[k] - self.temperature_out[k]) * self.cp * self.den

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class EnergyBalance(Constructed):
    """ calculates the energy consumption via MassFlows """

    def __init__(
            self,
            name:       str,
            heat_flows: Union[list[HeatFlow], list[Feature]],
            plt_opts:   Union[PlotOptions, None] = None,
    ):

        self.heat_flows: list[HeatFlow] = list()
        for flow in heat_flows:

            if isinstance(flow, Feature):
                if isinstance(flow.variable, HeatFlow):
                    self.heat_flows.append(flow.variable)

            elif isinstance(flow, HeatFlow):
                self.heat_flows.append(flow)
            else:
                raise ValueError('Make sure to pass a list of HeatFlows.')

        # default plot options
        if plt_opts is None:
            plt_opts = PlotOptions(
                color=fmt.black,
                line=fmt.line_solid,
            )

        Constructed.__init__(
            self,
            name=name,
            plt_opts=plt_opts,
        )

    @property
    def subs(self) -> list[Variable]:
        return self.heat_flows

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = float(sum(df.loc[row, heat_flow.col_name] for heat_flow in self.heat_flows))

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = sum(df[heat_flow] for heat_flow in self.heat_flows)

        return df

    def constraint(self, k: int) -> ca.MX:

        assert k in self.mx
        for heat_flow in self.heat_flows:
            assert k in heat_flow.mx

        lhs = self[k]
        rhs = ca.DM(0)

        for heat_flow in self.heat_flows:
            rhs += heat_flow[k]

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class Addition(Constructed):

    def __init__(
            self,
            b1: Union[Variable, Feature],
            b2: Union[Variable, Feature],
            plt_opts: Union[PlotOptions, None] = None,
    ):

        if isinstance(b1, Feature):
            b1 = b1.variable

        if isinstance(b2, Feature):
            b2 = b2.variable

        if plt_opts is None:
            plt_opts = b1.plt_opts

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({b1.name} - {b2.name})',
            plt_opts=plt_opts,
        )

        self.b1 = b1
        self.b2 = b2

    @property
    def subs(self) -> list[Variable]:
        return [self.b1, self.b2]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = float(df.loc[row, self.b1.col_name] + df.loc[row, self.b2.col_name])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df[self.b1.col_name] + df[self.b2.col_name]

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k not in self.b1.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.b1} which is base for {self}.')

        if k not in self.b2.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.b1} which is base for {self}.')

        lhs = self[k]
        rhs = self.b1[k] + self.b2[k]

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class Subtraction(Constructed):

    def __init__(
            self,
            b1: Union[Variable, Feature],
            b2: Union[Variable, Feature],
            plt_opts: Union[PlotOptions, None] = None,
    ):

        if isinstance(b1, Feature):
            b1 = b1.variable

        if isinstance(b2, Feature):
            b2 = b2.variable

        if plt_opts is None:
            plt_opts = b1.plt_opts

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({b1.name} - {b2.name})',
            plt_opts=plt_opts,
        )

        self.b1 = b1
        self.b2 = b2

    @property
    def subs(self) -> list[Variable]:
        return [self.b1, self.b2]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = float(df.loc[row, self.b1.col_name] - df.loc[row, self.b2.col_name])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df[self.b1.col_name] - df[self.b2.col_name]

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k not in self.b1.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.b1} which is base for {self}.')

        if k not in self.b2.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.b1} which is base for {self}.')

        lhs = self[k]
        rhs = self.b1[k] - self.b2[k]

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class Multiplication(Constructed):

    def __init__(
            self,
            b1: Union[Variable, Feature],
            b2: Union[Variable, Feature],
            plt_opts: Union[PlotOptions, None] = None,
    ):

        if isinstance(b1, Feature):
            b1 = b1.variable

        if isinstance(b2, Feature):
            b2 = b2.variable

        if plt_opts is None:
            plt_opts = b1.plt_opts

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({b1.name} - {b2.name})',
            plt_opts=plt_opts,
        )

        self.b1 = b1
        self.b2 = b2

    @property
    def subs(self) -> list[Variable]:
        return [self.b1, self.b2]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = float(df.loc[row, self.b1.col_name] * df.loc[row, self.b2.col_name])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df[self.b1.col_name] * df[self.b2.col_name]

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k not in self.b1.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.b1} which is base for {self}.')

        if k not in self.b2.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.b1} which is base for {self}.')

        lhs = self[k]
        rhs = self.b1[k] * self.b2[k]

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class Shift(Constructed):
    """ used to shift a feature back in time """

    def __init__(
            self,
            base:       Union[Variable, Feature],
            n:          int,
            plt_opts:   Union[PlotOptions, None] = None,
    ):

        if isinstance(base, Feature):
            base = base.variable

        if plt_opts is None:
            plt_opts = base.plt_opts

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({base.name}, n={n})',
            plt_opts=plt_opts,
        )

        self.base = base
        self.n = n

    @property
    def subs(self) -> list[Variable]:
        return [self.base]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        if idx <= self.n:
            return df

        row = df.index[idx]
        nth_row = df.index[idx-self.n]

        df.loc[row, self.col_name] = float(df.loc[nth_row, self.base.col_name])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        if self.base.col_name not in df.columns:
            df = self.base.process(df)

        df[self.col_name] = df[self.base.col_name].shift(self.n)

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k - self.n not in self.base.mx:
            print(k, 'not in', self.base.mx.keys(), 'base:', self.base)
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.base} which is base for {self}.')

        lhs = self[k]
        rhs = self.base[k - self.n]

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return self.n


class TimeFunc(Constructed):

    def __init__(
            self,
            name: str,
            func: Callable,
            plt_opts: Union[PlotOptions, None] = None,
    ):

        if plt_opts is None:
            plt_opts = PlotOptions(color=fmt.grey, line=fmt.line_dashed)

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({name})',
            plt_opts=plt_opts,
        )

        self.func: Callable = func

    @property
    def subs(self) -> list[Variable]:
        return []

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = self.func(df.loc[row, 'SimTime'])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df['SimTime'].apply(self.func)

        return df

    def constraint(self, k: int) -> ca.MX:

        raise NotImplementedError()

    @property
    def past_steps(self) -> int:
        return 0


class Func(Constructed):

    def __init__(
            self,
            name: str,
            func: Callable,
            base: Union[Variable, Feature],
            plt_opts: Union[PlotOptions, None] = None,
    ):
        if isinstance(base, Feature):
            base = base.variable

        if plt_opts is None:
            plt_opts = PlotOptions(color=fmt.grey, line=fmt.line_dashed)

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({name})',
            plt_opts=plt_opts,
        )

        self.func: Callable = func
        self.base: Variable = base

    @property
    def subs(self) -> list[Variable]:
        return [self.base]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]
        df.loc[row, self.col_name] = self.func(df.loc[row, self.base.col_name])

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df[self.col_name] = df[self.base.col_name].apply(self.func)

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k not in self.base.mx:
            print(k, 'not in', self.base.mx.keys(), 'base:', self.base)
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.base} which is base for {self}.')

        lhs = self[k]
        rhs = self.func(self.base[k])

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0


class ConstructedQuadratic(Constructed):
    """ used to calculate the change between to time steps """

    def __init__(
            self,
            base: Union[Variable, Feature],
            plt_opts: Union[PlotOptions, None] = None,
    ):

        if isinstance(base, Feature):
            base = base.variable

        if plt_opts is None:
            plt_opts = base.plt_opts

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({base.name})',
            plt_opts=plt_opts,
        )

        self.base = base

    @property
    def subs(self) -> list[Variable]:
        return [self.base]

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]

        df.loc[row, self.col_name] = float(df.loc[row, self.base.col_name]) ** 2

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        if self.base.col_name not in df.columns:
            df = self.base.process(df)

        df[self.col_name] = df[self.base.col_name] ** 2

        return df

    def constraint(self, k: int) -> ca.MX:

        if k not in self.mx:
            raise ValueError(f'Did not find k={k} in the keys of mx for {self}.')

        if k not in self.base.mx:
            print(k, 'not in', self.base.mx.keys(), 'base:', self.base)
            raise ValueError(f'Did not find k={k} in the keys of mx for {self.base} which is base for {self}.')

        lhs = self[k]
        rhs = self.base[k] ** 2

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 1

class Sum(Constructed):

    """ used to calculate the sum of multiple Sources """

    def __init__(
            self,
            name:       str,
            bases:      list[Union[Variable, Feature]],
            plt_opts:   PlotOptions,
    ):

        self.sources: list[Variable] = list()
        for base in bases:
            if isinstance(base, Feature):
                self.sources.append(base.variable)
            elif isinstance(base, Variable):
                self.sources.append(base)
            else:
                raise ValueError('Please only pass a list of Sources for Features!')

        Constructed.__init__(
            self,
            name=f'{self.__class__.__name__}({name})',
            plt_opts=plt_opts,
        )

    @property
    def n(self):
        return len(self.sources)

    def update(self, df: pd.DataFrame, idx: int) -> pd.DataFrame:

        row = df.index[idx]
        df.loc[row, self.col_name] = sum(df.loc[row, source.col_name] for source in self.sources)

        return df

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        try:
            df[self.col_name] = sum(df[source.col_name] for source in self.sources)

        except TypeError as e:

            print('col_names:', [source.col_name for source in self.sources])
            print('col_names:', [df[source.col_name] for source in self.sources])
            print('self.n:', self.n)

            raise e

        return df

    @property
    def subs(self) -> list[Variable]:
        return self.sources

    def constraint(self, k: int) -> ca.MX:

        for s in self.sources:
            assert k in s.mx

        lhs = self[k]

        rhs = ca.sum1(ca.vertcat(*[source[k] for source in self.sources]))

        return lhs - rhs

    @property
    def past_steps(self) -> int:
        return 0
