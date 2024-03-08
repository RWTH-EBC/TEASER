#!/usr/bin/env python

""" modes.py: Modes for the Control features. """

import abc
import datetime
import random
import numpy
from typing import Optional

import numpy as np
import pandas as pd
import sys
class Mode(abc.ABC):

    # timestamp of offset (Unix Time / seconds from 1.1.1970)
    # (Starting day of Simulation)
    # Monday: 1.1.2018-> 1514764800
    # Tuesday: 1.1.2019-> 1546300800
    # Wednesday: 1.1.2022 -> 1640995200
    # Thursday: 1.1.2015 -> 1420066800
    # Friday:  1.1.2021 -> 1609459200
    # Saturday: 1.1.2011 -> 1293840000
    # Sunday: 1.1.2017 -> 1483228800

    def __init__(
            self,
            day_start:      int = 8,
            day_end:        int = 16,
            time_offset:    int = 0
    ):

        self.day_start: int = day_start
        self.day_end:   int = day_end

        self.time_offset: int = time_offset

    def __str__(self):
        return f'Mode({self.__class__.__name__})'

    def __repr__(self):
        return f'Mode({self.__class__.__name__})'

    @abc.abstractmethod
    def error(self, time: int, value: float) -> float:
        """ Returns the control error """
        ...

    @abc.abstractmethod
    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """
        ...

    def lb(self, time: int) -> float:
        return self.bounds(time)[0]

    def ub(self, time: int) -> float:
        return self.bounds(time)[1]

    @abc.abstractmethod
    def target(self, time: int) -> float:
        """ returns the control target for a given time """
        ...

    def _day(self, time: int) -> bool:
        """ returns True if the given time is during day """

        time = datetime.datetime.fromtimestamp(self.time_offset + time)

        return self.day_start <= time.hour < self.day_end

    def _weekend(self, time: int) -> bool:
        """ returns True if the given time is during weekend """

        time = datetime.datetime.fromtimestamp(self.time_offset + time)

        return 5 <= time.weekday()

    def _presence(self, time:int, schedules) -> bool:
        """ returns True if the given time is during presence periods """

        time = datetime.datetime.fromtimestamp(self.time_offset + time)
        try:
            if schedules.loc[time].persons_profile > 0:
                return True
            else:
                return False
        except: #workaround, because last hour in schedules dataframe is not filled with data
            return False


class Steady(Mode):
    """ steady values for day and night """

    def __init__(
            self,
            day_start:      int = 8,
            day_end:        int = 16,
            day_target:     float = 273.15 + 20,
            night_target:   float = 273.15 + 18,
            time_offset:    int = 0,
            weekend:        bool = True,
    ):

        super(Steady, self).__init__(day_start=day_start, day_end=day_end, time_offset=time_offset)

        self.day_target = day_target
        self.night_target = night_target

        self.weekend = weekend

    def error(self, value: float, time: int) -> float:
        """ Returns the control error """

        return self.target(time) - value

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        return numpy.nan, numpy.nan

    def target(self, time: int) -> float:
        """ returns the control target for a given time """

        if self._weekend(time) and self.weekend:
            return self.night_target

        if self._day(time):
            return self.day_target

        return self.night_target


class Random(Mode):
    """ random sequence of set points between bounds """

    def __init__(
            self,
            day_start:      int = 8,
            day_end:        int = 16,
            day_lb:         float = 273.15 + 19,
            night_lb:       float = 273.15 + 16,
            day_ub:         float = 273.15 + 21,
            night_ub:       float = 273.15 + 24,
            interval:       int = 60 * 60 * 4,
            time_offset:    int = 0,
    ):

        super(Random, self).__init__(day_start=day_start, day_end=day_end, time_offset=time_offset)

        self.day_lb:    float = day_lb
        self.night_lb:  float = night_lb
        self.day_ub:    float = day_ub
        self.night_ub:  float = night_ub

        self.interval:              int = interval
        self.last_randomization:    Optional[int] = None
        self.current_target:        Optional[int] = None

    def error(self, value: float, time: int) -> float:
        """ Returns the control error """

        return self.target(time) - value

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        if self._weekend(time):
            return self.night_lb, self.night_ub

        if self._day(time):
            return self.day_lb, self.day_ub

        return self.night_lb, self.night_ub

    def target(self, time: int) -> float:
        """ returns the control target for a given time """

        lb, ub = self.bounds(time)

        if self.last_randomization is None:
            self.last_randomization = time

        if self.current_target is None:
            self.current_target = random.uniform(lb, ub)

        def new_target():

            target = random.uniform(lb, ub)

            if abs(self.current_target - target) < 1:
                target = new_target()

            return target

        time_over = time - self.last_randomization >= self.interval
        no_target = self.current_target is None
        target_too_small = self.current_target < lb
        target_too_big = ub < self.current_target

        if time_over or no_target or target_too_big or target_too_small:

            self.current_target = new_target()
            self.last_randomization = time

        return self.current_target


class Identification(Mode):
    """ random sequence of set points between bounds """

    def __init__(
            self,
            day_start:      int = 8,
            day_end:        int = 16,
            day_lb:         float = 273.15 + 19,
            night_lb:       float = 273.15 + 16,
            day_ub:         float = 273.15 + 21,
            night_ub:       float = 273.15 + 24,
            time_offset:    int = 0,

            min_interval:   float = 60 * 60 * 1,
            max_interval:   float = 60 * 60 * 5,
            min_change:     float = 0.5,
            max_change:     float = 3,
    ):

        super(Identification, self).__init__(day_start=day_start, day_end=day_end, time_offset=time_offset)

        self.day_lb:    float = day_lb
        self.night_lb:  float = night_lb
        self.day_ub:    float = day_ub
        self.night_ub:  float = night_ub

        self.max_interval:          int = max_interval
        self.min_interval:          int = min_interval
        self.interval:              int = random.randrange(min_interval, max_interval)
        self.min_change:            int = min_change
        self.max_change:            int = max_change

        self.last_randomization:    Optional[int] = None
        self.current_target:        Optional[int] = None

    def error(self, value: float, time: int) -> float:
        """ Returns the control error """

        return self.target(time) - value

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        if self._weekend(time):
            return self.night_lb, self.night_ub

        if self._day(time):
            return self.day_lb, self.day_ub

        return self.night_lb, self.night_ub

    def target(self, time: int) -> float:
        """ returns the control target for a given time """

        lb, ub = self.bounds(time)

        if self.last_randomization is None:
            self.last_randomization = time

        if self.current_target is None:
            self.current_target = random.randint(int(lb), int(ub))

        def new_target():

            max_pos_change = min(abs(ub - self.current_target), self.max_change)
            min_pos_change = min(abs(ub - self.current_target), self.min_change)

            max_neg_change = min(abs(lb - self.current_target), self.max_change)
            min_neg_change = min(abs(lb - self.current_target), self.min_change)

            pos_change = random.uniform(a=min_pos_change, b=max_pos_change)
            neg_change = - random.uniform(a=min_neg_change, b=max_neg_change)

            if self.current_target + self.min_change > ub:
                c = neg_change
            elif self.current_target - self.min_change < lb:
                c = pos_change
            else:
                c = random.choice([pos_change, neg_change])

            target = self.current_target + c

            return target

        if time - self.last_randomization >= self.interval or\
                self.current_target is None or\
                self.current_target < lb or\
                ub < self.current_target:

            new_target = new_target()
            change = self.current_target - new_target
            frac = (self.max_change - abs(change)) / (self.max_change - self.min_change)
            self.interval = int(self.min_interval + (1 - frac) * (self.max_interval - self.min_interval))

            self.current_target = new_target
            # self.interval = int(random.uniform(self.min_interval, self.max_interval))

            self.last_randomization = time

        return self.current_target


class Economic(Mode):
    """ bounds for day and night """

    def __init__(
            self,
            day_start:  int = 8,
            day_end:    int = 16,
            day_lb:     float = 273.15 + 19,
            day_ub:     float = 273.15 + 22,
            night_lb:   float = 273.15 + 16,
            night_ub:   float = 273.15 + 25,
            weekend:    bool = True,
            time_offset: int = 0,
    ):

        super(Economic, self).__init__(day_start=day_start, day_end=day_end, time_offset=time_offset)

        self.day_lb:    float = day_lb
        self.night_lb:  float = night_lb
        self.day_ub:    float = day_ub
        self.night_ub:  float = night_ub

        self.weekend:   bool = weekend

    def error(self, value: float, time: int) -> float:
        """ Returns the control error """

        lb, ub = self.bounds(time)

        if value < lb:
            return lb - value

        if value > ub:
            return ub - value

        return 0

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        if self._weekend(time) and self.weekend:
            return self.night_lb, self.night_ub

        if self._day(time):
            return self.day_lb, self.day_ub

        return self.night_lb, self.night_ub

    def target(self, time: int) -> float:
        """ returns the control target for a given time """

        return numpy.nan


class Power(Mode):

    def __init__(
            self,
    ):

        super(Power, self).__init__(day_start=8, day_end=16)

    def error(self, value: float, time: int) -> float:
        """ Returns the control error """

        lb, ub = self.bounds(time)

        if value < lb:
            return lb - value

        if value > ub:
            return ub - value

        return 0

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        return np.nan, np.nan

    def target(self, time: int) -> float:
        """ returns the control target for a given time """

        return 0


class NoMode(Mode):

    def __init__(self):

        super(NoMode, self).__init__(day_start=np.nan, day_end=np.nan)

    def error(self, time: int, value: float) -> float:
        """ Returns the control error """
        return 0

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        return np.nan, np.nan

    def target(self, time: int) -> float:
        """ returns the control target for a given time """
        return np.nan

class Economic_Presence(Mode):
    """ dynamic bounds based on presence schedules from TEASER """

    def __init__(
            self,
            presence_lb:     float = 273.15 + 20,
            presence_ub:     float = 273.15 + 22,
            absence_lb:   float = 273.15 + 16,
            absence_ub:   float = 273.15 + 25,
            time_offset: int = 0,
            schedule_path = None
    ):

        super(Economic_Presence, self).__init__(time_offset=time_offset)

        self.presence_lb:    float = presence_lb
        self.absence_lb:  float = absence_lb
        self.presence_ub:    float = presence_ub
        self.absence_ub:  float = absence_ub

        # import schedules from pickle and set year to 1970 to match with simulation time and resample to step size
        #TODO: implement dynamic step size
        self.schedules = pd.read_pickle(schedule_path)
        self.schedules.index = pd.to_datetime(self.schedules.index, format="%m-%d %H:%M:%S")
        self.schedules.index = self.schedules.index.map(lambda t: t.replace(year=1970))
        self.schedules = self.schedules.resample("15min").fillna('nearest')


    def error(self, value: float, time: int) -> float:
        """ Returns the control error """

        lb, ub = self.bounds(time)

        if value < lb:
            return lb - value

        if value > ub:
            return ub - value

        return 0

    def bounds(self, time: int) -> tuple[float, float]:
        """ returns the lower and upper bound for a given time """

        if self._presence(time,schedules=self.schedules):
            return self.presence_lb, self.presence_ub

        else:
            return self.absence_lb, self.absence_ub

    def target(self, time: int) -> float:
        """ returns the control target for a given time """

        return numpy.nan
