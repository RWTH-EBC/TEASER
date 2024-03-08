import datetime
from threading import Lock
import sys


print_lock = Lock()

SILENT = 0
NORMAL = 1
FAIL = 2
WARN = 3
DEBUG = 4


def _print(message: str, end: str = None):

    with print_lock:
        if end is not None:

            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write(message)
            sys.stdout.flush()


        else:
            print(message)


class Logger:

    prefixes: list[str] = list()

    def __init__(
            self,
            prefix: str,
            level: int = DEBUG,
    ):

        self.prefix:        str = prefix
        self.prefix_len:    int = len(prefix)
        self.level:         int = level

        self.prefixes.append(prefix)

    def __call__(self, message: str, level: int = NORMAL, color: str = None, repeat: bool = False):
        """Thread safe print function"""

        if self.level >= level:

            spaces = ' ' * (self.max_prefix_length - self.prefix_len)
            now = datetime.datetime.now()

            if color is None:

                message = f'{now.strftime("%H:%M:%S")} {self.prefix} {spaces}| {message}'
                # print('message:', message, 'level', level, 'spaces', len(spaces))

            else:

                ENDC = '\033[0m'
                message = f'{now.strftime("%H:%M:%S")} {self.prefix} {spaces}| {color}{message}{ENDC}'

            if repeat:
                _print(message, end='')
            else:
                _print(message)

    @property
    def max_prefix_length(self):
        return max(len(prefix) for prefix in self.prefixes)
