import time
import numpy as np
import sys

# plt colors
dark_red = [172 / 255, 43 / 255, 28 / 255]
red = [221 / 255, 64 / 255, 45 / 255]
light_red = [235 / 255, 140 / 255, 129 / 255]
green = [112 / 255, 173 / 255, 71 / 255]
light_green = [171 / 255, 255 / 255, 115 / 255]
light_grey = [217 / 255, 217 / 255, 217 / 255]
grey = [157 / 255, 158 / 255, 160 / 255]
dark_grey = [78 / 255, 79 / 255, 80 / 255]
light_blue = [157 / 255, 195 / 255, 230 / 255] # 9DC3E6
blue = [0 / 255, 84 / 255, 159 / 255]
black = [0, 0, 0]
white = [255 / 255, 255 / 255, 255 / 255]
ebc_palette_sort_1 = [dark_red, red, light_red, dark_grey, grey, light_grey, blue, light_blue, green]
ebc_palette_sort_2 = [red, blue, grey, green, dark_red, dark_grey, light_red, light_blue, light_grey]

# linestyles
line_solid = '-'
line_dotted = ':'
line_dashed = '--'
line_dashdot = '-.'

# console colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd=''):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd, )
    # Print New Line on Complete
    if iteration == total:
        print()

def print_lists(*lst, statement):
    print(f'{BOLD}{statement}{ENDC}')
    for i, elements in enumerate(zip(*lst)):
        print('\t', "%03d" % i, *elements)


def generate_matrix(rows):
    max_length = max([len(row) for row in rows])
    for row in rows:
        for i in range(max_length - len(row)):
            row.append(0)
    return rows


def print_table_line(row: list, max_lengths: list, space_char: str = ' ', space_between_columns: str = '    '):
    print_string = ''

    if len(row) == 1:
        print(row[0])
        return

    for value, max_length in zip(row, max_lengths):
        value = str(value)
        max_length = int(max_length)

        print_string += value
        print_string += space_char * (max_length - len(value))
        print_string += space_between_columns

    print(print_string)


def print_table(rows: list, space_char: str = ' ', space_between_columns: str = '\t'):
    lengths = list()

    for row in rows:
        lengths.append([len(str(value)) for value in row if len(row) > 1])

    max_lengths = list(np.amax(generate_matrix(lengths), axis=0))

    for row in rows:
        print_table_line(row, max_lengths, space_char, space_between_columns)


def print_progress(i: int, n: int, text: str):
    j = (i + 1) / n

    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write(f"{text} [%-20s] %d%%" % ('=' * int(20 * j), 100 * j))
    sys.stdout.flush()


def interpolate_colors(i, colors):
    if i <= 0:
        return colors[0]
    elif i >= 1:
        return colors[-1]

    num_colors = len(colors)
    interval = 1 / (num_colors - 1)
    color_index = int(i / interval)
    t = (i - interval * color_index) / interval
    color1 = colors[color_index]
    color2 = colors[color_index + 1]
    return [(1 - t) * color1[0] + t * color2[0],
            (1 - t) * color1[1] + t * color2[1],
            (1 - t) * color1[2] + t * color2[2]
            ]
