from configparser import ConfigParser
from typing import Union, Callable, Any

import paho.mqtt.client
from datetime import datetime

import ddmpc.utils.parsing as parsing
from ddmpc.utils.logging import Logger, DEBUG, SILENT, FAIL, WARN, NORMAL


class MQTTClient(paho.mqtt.client.Client):

    def __init__(
            self,
            host:           str,
            port:           Union[int, str],

            client_id:      str,
            password:       str,
            username:       str,

            parser:         Union[parsing.Parser, str],
            log_level:      int = NORMAL,

            ca_certs:       Any = None,
            tls_version:    Any = None,

    ):

        super(MQTTClient, self).__init__(
            client_id=client_id,
            clean_session=True,
        )

        self.tls_set(ca_certs=ca_certs, tls_version=tls_version)
        self.username_pw_set(username=username, password=password)
        self.connect(host=host, port=port)

        self.callbacks: list[Callable] = list()

        def on_message(client, userdata, message: paho.mqtt.client.MQTTMessage):

            name, value, time = self.parser.decode(message.payload)

            for callback in self.callbacks:
                callback(name, value, time)

        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))

        self.on_message = on_message
        self.on_connect = on_connect

        if isinstance(parser, str):
            parser = parsing.from_name(parser)

        self.parser = parser
        self.logger = Logger(prefix=str(self), level=log_level)

    def __str__(self):
        return f'MQTTClient(client_id={self._client_id})'

    def __repr__(self):
        return f'MQTTClient(client_id={self._client_id})'

    def add_callback(self, callback: Callable):

        self.callbacks.append(callback)

    def publish_controls(
            self,
            topic:      str,
            name:       str,
            value:      Union[float, int, bool],
            time:       datetime,

            qos:        int = 0,
            dryrun:     bool = False,
    ) -> paho.mqtt.client.MQTTMessageInfo:

        topic = f'CONTROLS/{topic}'
        payload = self.parser.encode(name=name, value=value, time=time)

        self.logger(message=f'Publishing: topic={topic}, payload={payload}', level=DEBUG)

        if dryrun:
            return paho.mqtt.client.MQTTMessageInfo(mid='Successful dryrun')

        message_info: paho.mqtt.client.MQTTMessageInfo = self.publish(
            topic=topic,
            payload=payload,
            qos=qos,
            retain=False,
        )

        return message_info

    def publish_data(
            self,
            topic:      str,
            name:       str,
            value:      Union[float, int, bool],
            time:       datetime,
            qos:        int = 0,
            dryrun:     bool = False,
    ) -> paho.mqtt.client.MQTTMessageInfo:

        payload = self.parser.encode(name=name, value=value, time=time)

        self.logger(message=f'Publishing: topic={topic}, payload={payload}', level=DEBUG)

        if dryrun:
            paho.mqtt.client.MQTTMessageInfo(mid='Successful dryrun')

        message_info: paho.mqtt.client.MQTTMessageInfo = self.publish(
            topic=topic,
            payload=payload,
            qos=qos,
            retain=False,
        )

        return message_info


def MQTTClient_from_config(filepath: str = None, **kwargs) -> MQTTClient:

    if filepath is None:

        filepath = r'C:\Users\mbe\Documents\GitRepos\development-mbe-ma\Examples\EONERC\Aedifion\SeminarRooms\only_identification\config\mqtt_config.ini'

    config = ConfigParser()
    config.read(filepath)

    # create a dict of all subjects
    dct = {s: dict(config.items(s)) for s in config.sections()}

    mqtt_config: dict = dct['mqtt']

    try:
        mqtt_config['log_level'] = int(mqtt_config['log_level'])
    except KeyError:
        pass

    try:
        mqtt_config['port'] = int(mqtt_config['port'])
    except:
        pass

    for k, v in kwargs.items():
        mqtt_config[k] = v

    for tag in ['host', 'port', 'password', 'username', 'client_id', 'parser']:

        assert tag in mqtt_config.keys(), f'MQTT Config must include {tag}.'

    return MQTTClient(**mqtt_config)


def load_mqtt_config(filepath: str) -> dict:

    config = ConfigParser()
    config.read(filepath)

    # create a dict of all subjects
    dct = {s: dict(config.items(s)) for s in config.sections()}

    mqtt_config: dict = dct['mqtt']

    for tag in ['host', 'port', 'password', 'username', 'parser']:

        assert tag in mqtt_config.keys(), f'MQTT Config must include {tag}.'
    try:
        mqtt_config['log_level'] = int(mqtt_config['log_level'])
    except KeyError:
        pass

    try:
        mqtt_config['port'] = int(mqtt_config['port'])
    except KeyError:
        pass

    return mqtt_config


if __name__ == '__main__':

    client = MQTTClient_from_config()

