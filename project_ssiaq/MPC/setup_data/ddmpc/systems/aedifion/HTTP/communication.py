import json
import time
from typing import Optional, Union, Iterator
import datetime

import numpy as np
import pandas as pd
import pytz
import requests


auth_filepath = r'C:\Users\mbe\Documents\GitRepos\development-mbe-ma\Examples\EONERC\Aedifion\auth.json'


def read_auth() -> tuple[str, str]:

    with open(auth_filepath) as f:
        d = json.load(f)

        return d['username'], d['password']


class DataPointInfo:

    def __init__(self, response: requests.Response):

        json_response = response.json()

        if True:
            print(f'There are {len(json_response["tags"])} tags.')
            for t in json_response['tags']:
                print(t)

        self.dataPointID: str = json_response['dataPointID']
        self.description: Optional[str] = None
        self.units: Optional[str] = None
        self.min_pres_value: Optional[float] = None
        self.max_pres_value: Optional[float] = None

        for t in json_response['tags']:

            key = t['key']
            value = t['value']
            """
            match key:
                case 'units':
                    self.units = value
                case 'description':
                    self.description = value
                case 'update-interval':
                    self.update_interval = value
                case 'min-pres-value' | 'minPresValue':
                    self.min_pres_value = value
                case 'max-pres-value' | 'maxPresValue':
                    self.max_pres_value = value
                case 'device-type':
                    self.device_type = value
                case 'resolution':
                    self.resolution = value
                case 'device_id':
                    self.device_id = value
                case 'reliability':
                    self.reliability = value
                case 'objtype':
                    self.objtype = value
                case 'out-of-service':
                    self.out_of_service = value
                case 'number-of-states':
                    self.number_of_states = value
                case 'state-text':
                    self.state_text = value
                case 'present-value':
                    self.present_value = value
                
            """

    def summary(self):

        print('DataPointInfo:')

        for key, val in vars(self).items():
            print(f'\t{key}: {val}')

        print()

    def __str__(self):

        return f'DataPointInfo({self.description})'

    def __repr__(self):
        return f'DataPointInfo'


class DataPoint:

    default_domain = 'https://api.ercebc.aedifion.io'
    default_path = '/v2/datapoint'
    default_projectID = 11
    default_priority = 11
    default_timezone = pytz.timezone('Europe/Berlin')

    def __init__(
            self,
            feedbackID:     str,
            setPointID:     Optional[str] = None,
            domain:         str = default_domain,
            path:           str = default_path,
            projectID:      int = default_projectID,
            step:           bool = False,
            offset:         float = 0,
    ):
        self.feedbackID:    str = feedbackID
        self.setPointID:    str = setPointID
        self.projectID:     int = projectID

        self.domain:        str = domain
        self.path:          str = path

        self.step:          bool = step
        self.offset:        float = offset

    def summary(self):
        """ Prints short summary """

        data_point_info = DataPointInfo(self._getResponse())
        data_point_info.summary()

    def getLastValue(self):

        response = self._getTimeSeriesResponse(
            end=datetime.datetime.now(),
            max_n=1,
            short=True,
        ).json()

        return response[0][1] + self.offset

    def getDataPointInfo(self) -> DataPointInfo:
        """ Returns a DataPointInfo Object """

        return DataPointInfo(self._getResponse())

    def getTimeSeriesAedifionInterpolation(
            self,
            samplerate:     int,
            period:         Optional[int] = None,
            start:          Optional[datetime.datetime] = None,
            end:            Optional[datetime.datetime] = None,
    ) -> pd.Series:
        """ Efficient way to get the past data as a Pandas Series (aedifion interpolation and resampling) """

        if period is None and start is None:
            raise ValueError('Make sure to pass either "period" or "start".')

        if end is None:
            end = datetime.datetime.now()

        if start is None:
            start = end - datetime.timedelta(seconds=period)

        response = self._getTimeSeriesResponse(
            samplerate=samplerate,
            start=start,
            end=end,
            short=True,
            interpolation='linear',
            aggregation='mean',
            closed_interval=True,
        )

        series = self._responseToSeries(response)

        return series + self.offset

    def getTimeSeriesRaw(
            self,
            period:             Optional[int] = None,
            start:              Optional[datetime.datetime] = None,
            end:                Optional[datetime.datetime] = None,
    ) -> pd.Series:
        """ Returns all measured data for the given time span without interpolation or resampling"""

        if period is None and start is None:
            raise ValueError('Make sure to pass either "period" or "start".')

        if end is None:
            end = datetime.datetime.now(tz=self.default_timezone)

        if start is None:
            start = end - datetime.timedelta(seconds=period)

        if end < start:
            raise ValueError(f'The start date ({start}) is before the end date({end}).')

        response = self._getTimeSeriesResponse(
            samplerate=60,
            start=start,
            end=end,
            short=True,
            interpolation='none',
            closed_interval=True,
        )

        # convert Response to pd.Series() with pd.DatetimeIndex
        series = self._responseToSeries(response)

        return series + self.offset

    def getTimeSeriesOwnInterpolation(
            self,
            samplerate:     int,
            start:          datetime.datetime,
            end:            datetime.datetime,
    ) -> pd.Series:

        # localize the start and end time
        if start.tzinfo is None:
            start = self.default_timezone.localize(start)

        if end.tzinfo is None:
            end = self.default_timezone.localize(end)

        # get the raw time series
        series = self.getTimeSeriesRaw(
            start=start,
            end=end,
        )

        # resample to one minute
        series = series.resample(
            rule=datetime.timedelta(seconds=60),
        ).mean()

        # fill nan
        if self.step:
            series.fillna(method='ffill', inplace=True)

        else:
            series.interpolate(inplace=True)

        # resample to desired samplerate
        series = series.resample(
            rule=datetime.timedelta(seconds=samplerate),
            label='right',
            closed='right',
            origin=end-datetime.timedelta(seconds=samplerate / 2),
        ).mean()

        # shift index by half the samplerate
        series.index = series.index - datetime.timedelta(seconds=samplerate / 2)

        return series

    def _responseToSeries(self, response: requests.Response) -> pd.Series:

        # raise for status, if error occurred
        response.raise_for_status()

        # transform data to a DataFrame
        df = pd.DataFrame(response.json(), columns=['time', self.feedbackID])

        # create a new the DatetimeIndex
        datetime_series = pd.to_datetime(df['time'])
        datetime_index = pd.DatetimeIndex(datetime_series.values)

        # first localize at gmt
        gmt = pytz.timezone("Etc/GMT")
        datetime_index = datetime_index.tz_localize(gmt)

        # convert to german time
        berlin = pytz.timezone('Europe/Berlin')
        datetime_index = datetime_index.tz_convert(berlin)

        # set DatetimeIndex as index
        df = df.set_index(datetime_index)
        df.drop('time', axis=1, inplace=True)

        return df[self.feedbackID]

    def _getResponse(self) -> requests.Response:
        """
        Gets the data point including meta information, i.e., whether it is a user's favorite, its renamings and tags.
        """

        params = {
            'dataPointID': self.feedbackID,
            'project_id': self.projectID,
        }

        response = requests.get(url=f'{self.domain}/{self.path}', params=params, auth=read_auth())

        response.raise_for_status()

        return response

    def _getTimeSeriesResponse(
            self,
            samplerate:         int = None,
            start:              Optional[datetime.datetime] = None,
            end:                Optional[datetime.datetime] = None,
            max_n:              Optional[int] = None,
            interpolation:      str = 'null',
            aggregation:        str = 'mean',
            closed_interval:    bool = False,
            short:              bool = False,

    ) -> requests.Response:
        """
        Returns the measured time series data for the specified data point referenced by its name/dataPointID
        for the time interval specified by start and end. Returns the last (or respectively next) max observations,
        if either start nor end are provided.

        :param start:           Return only observations after this date-time.
                                If start is provided without end, the first max elements after start are returned.
        :param end:             Return only observations before this date-time.
        :param max_n:           If end is provided without start, the last max elements before end are returned.

        :param samplerate:      Maximum number of observations to return.
                                This option is ignored when both start and end are provided.
                                Setting max = 0 returns all available data points.
        :param interpolation:   Desired sampling rate. The returned observations are sampled down to the specified
                                interval. The down sampling will be done by calculating the arithmetic average on all
                                observations made within an interval. The timestamp will represent the beginning
                                of the interval the resampling average is estimated for.
                                Allowed: 'previous', 'linear', 'null', 'none'
        :param aggregation:     Desired interpolation method. Allowed: 'mean', 'min', 'max', 'mode', 'median'
        :param short:           Desired aggregation method.
        """

        params = {
            'dataPointID':      self.feedbackID,
            'project_id':       self.projectID,
            'interpolation':    interpolation,
            'aggregation':      aggregation,
            'closed_interval':  closed_interval,
            'short':            short,
        }

        if samplerate is not None:
            params['samplerate'] = f'{samplerate}s'

        if start is not None:
            params['start'] = start

        if end is not None:
            params['end'] = end

        if max_n is not None:
            params['max_n'] = max_n

        url = f'{self.domain}/{self.path}/timeseries'

        auth = read_auth()

        response = requests.get(
            url=url,
            params=params,
            auth=auth,
        )
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise requests.HTTPError(f'Failed to get Timeseries for {self.feedbackID}: {e}')

        return response

    def postSetPoint(
            self,
            value:      Union[float, str, bool],
            priority:   Optional[str] = None,
            acked:      bool = True,
            dryrun:     bool = False,
    ) -> requests.Response:
        """
        Attempts to write 'value' with given 'priority' to the DataPoint.

        :param value: The dataPointID of the data point for which to write a setpoint.
        :param priority: The numeric id of the project which the data point identified by 'dataPointID' belongs to.
        :param acked: Request acknowledgement for SetPoint write operation.
        :param dryrun: Do a dry run without actually writing anything.
        """

        assert self.setPointID is not None, f'{self} cant be set.'

        if priority is None:
            priority = self.default_projectID

        params = {
            'dataPointID': self.setPointID,
            'project_id': self.projectID,
            'value': value,
            'priority': priority,
            'acked': acked,
            'dryrun': dryrun,
        }

        print('post:', params)
        time.sleep(2)
        res = requests.post(f"{self.domain}/{self.path}/setpoint", auth=read_auth(), params=params)

        res.raise_for_status()

        print('response:', res.json())

        return res

    def __str__(self):
        return f'DataPoint(feedbackID: {self.feedbackID}, setPointID: {self.setPointID}, project_id: {self.projectID})'

    def __repr__(self):
        return f'DataPoint(feedbackID: {self.feedbackID}, setPointID: {self.setPointID}, project_id: {self.projectID})'


class VirtualDataPoint:

    def __init__(self):

        super(VirtualDataPoint, self).__init__()


class AedifionClient:

    def __init__(
            self,
            dataPoints: list[DataPoint],
    ):

        self.dataPoints: list[DataPoint] = dataPoints

    def getTimeSeries(
            self,
            samplerate:     int,
            start:          datetime.datetime,
            end:            Optional[datetime.datetime] = None,
            include_unix:   bool = False,
    ) -> pd.DataFrame:
        """ Efficient way to get the past data for multiple DataPoints as a Pandas Series """

        if end is None:
            end = datetime.datetime.now()

        series_lst = list()

        # get raw values points for all DataPoints
        for dataPoint in self:

            series = dataPoint.getTimeSeriesOwnInterpolation(
                samplerate=samplerate,
                start=start,
                end=end,
            )

            series_lst.append(series)

        # concat to DataFrame
        df = pd.concat(series_lst, axis=1)

        if include_unix:

            df['SimTime'] = df.index.astype(np.int64) // 10 ** 9
            df.reset_index(inplace=True, drop=True)

        return df

    def getTimeSeriesRaw(
            self,
            period: Optional[int] = None,
            start: Optional[datetime.datetime] = None,
            end: Optional[datetime.datetime] = None,
    ) -> pd.DataFrame:

        series_lst = list()

        # get raw values points for all DataPoints
        for dataPoint in self:

            series = dataPoint.getTimeSeriesRaw(
                period=period,
                start=start,
                end=end,
            )

            series_lst.append(series)

        # concat to DataFrame
        df = pd.concat(series_lst, axis=1)

        return df

    def getLastValues(self) -> dict:
        """ Returns the last measured values for all DataPoint's """

        values = dict()

        for dp in self.dataPoints:
            try:
                values[dp.feedbackID] = dp.getLastValue()
            except Exception as e:
                raise ValueError(f'An error occurred, while gathering the lastValue for {dp}: {e}')

        return values

    def summary(self):

        print('AedifionClient:')
        for dataPoint in self:
            print(f'\t{dataPoint}')
        print()

    def __getitem__(self, item: int) -> DataPoint:
        return self.dataPoints[item]

    def __iter__(self) -> Iterator[DataPoint]:
        return iter(self.dataPoints)

    def __str__(self):

        return f'AedifionClient({len(self.dataPoints)} DataPoints)'

    def __repr__(self):

        return f'AedifionClient({len(self.dataPoints)} DataPoints)'

