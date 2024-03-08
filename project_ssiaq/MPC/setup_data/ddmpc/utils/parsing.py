import datetime
from typing import Union
from abc import ABC, abstractmethod

from paho.mqtt.client import MQTTMessage
from line_protocol_parser import parse_line
import json


class DecodeError(Exception):

    def __init__(self, payload):

        message = f'Payload could not be decoded: {payload}'

        super(DecodeError, self).__init__(message)


class Parser(ABC):

    @abstractmethod
    def decode_control(self, message: MQTTMessage) -> tuple[str, Union[float, int, bool], datetime.datetime]:
        """ Decodes a MQTTMessage in SWOP format to a tuple of (name, value, timestamp) """

    @abstractmethod
    def decode(self, message: MQTTMessage) -> tuple[str, Union[float, int, bool], datetime.datetime]:
        """ Decodes a MQTTMessage to a tuple of (name, value, timestamp) """

        pass

    @abstractmethod
    def encode(self, name: str, value: Union[float, int, bool], time: datetime.datetime):
        """ Encodes a tuple of (name, value, timestamp) to an MQTTMessage """

        pass


class InfluxDBLine(Parser):

    def decode_control(self, message: MQTTMessage) -> tuple[str, Union[float, int, bool], datetime.datetime]:

        payload = message.payload.decode("utf-8")

        try:

            data = json.loads(payload)

            if data['type'] != 'NEWSPT':
                raise DecodeError(payload)

            name = data['datapoint']
            value = data['value']
            time = datetime.datetime.now()

        except:
            raise DecodeError(payload)

        return name, value, time

    def decode(self, message: MQTTMessage) -> tuple[str, Union[float, int, bool], datetime.datetime]:

        payload = message.payload.decode("utf-8")

        try:

            data = parse_line(payload)

            name = data["measurement"]
            value = data["fields"]["value"]
            time = datetime.datetime.fromtimestamp(data["time"] * (10**-9))

        except:

            raise DecodeError(payload)

        return name, value, time

    def encode(self, name: str, value: Union[float, int, bool], time: datetime.datetime):

        # timestamp in nanoseconds
        timestamp = int(time.timestamp() * 10 ** 9)

        return f"{name} value={value} {timestamp}"


def from_name(name: str) -> Parser:

    parser_map = {
        'influxdbline': InfluxDBLine,
    }

    try:
        parser = parser_map[name.lower()]

    except KeyError:
        raise KeyError(f'The given parser is unknown: {name}')

    return parser()
