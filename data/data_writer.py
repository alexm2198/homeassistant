#!/usr/bin/python3
from datetime import datetime


# Random generator of values. Each value is generated in a delta t = 1 second and in (0,30) range.
def data_writer(file_to_write, parameter):
    try:
        open(file_to_write, 'r')
    except FileNotFoundError:
        open(file_to_write, 'x')

    time_axis = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
    open(file_to_write, "a").write(f'{time_axis},{parameter}\n')

# data_writer('universal/universal_data_' + date.today().strftime("%d-%m-%Y") + '.txt')
