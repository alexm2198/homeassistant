#!/usr/bin/python3
from matplotlib import pyplot, dates
from matplotlib import animation
from datetime import date, datetime
from utils import globals
import numpy as np
from graphs import get_sensor_value
import os
from pathlib import Path


# !!! TIME INTERVAL FOR PLOTTING: 1 sec = 0.00001157 time units
time_unit = 0.00001157

fig = pyplot.figure('Last Week Data - Homeassistant', figsize=(10, 7))
pyplot.style.use("ggplot")
# format for X -axis displaying only hours and minutes
myFormat = dates.DateFormatter('%d-%m-%Y %H:%M')

# Paths to data collected
temp_path = Path(os.getcwd() + r"/data/temperature/")
hum_path = Path(os.getcwd() + r"/data/humidity/")


def extract_datetime_from_file_name(data_file):
    data_file = str(data_file)
    date_time = data_file.split("_")
    date_time =date_time[len(date_time) - 1].replace('.txt', '')
    return date_time


# returns two lists of equal size which represent x_coordonates and y_coordonates extracted
# from the given path
def extract_data_from_files(path_to_data_file):
    xs = []
    ys = []
    for file in path_to_data_file.glob("*.txt"):
        file_date_time = extract_datetime_from_file_name(file)
        data = open(file, "r").read()
        lines = data.split("\n")
        for coord in lines:
            if len(coord) > 1:
                x_vals, y_vals = coord.split(",")
                if y_vals != 'None':
                    x_vals = x_vals + ' ' + file_date_time
                    xs.append(datetime.strptime(x_vals, "%H:%M:%S %d-%m-%Y"))
                    ys.append(float(y_vals))
    return xs, ys


temp_xs, temp_ys = extract_data_from_files(temp_path)
hum_xs, hum_ys = extract_data_from_files(hum_path)

ax = pyplot.subplot()
ax.xaxis_date()
ax.xaxis.set_major_formatter(myFormat)
x_dates = dates.date2num(temp_xs)
ax.set_xlim(left=x_dates[len(x_dates) - 1] - np.float64(3600*24*7*time_unit),
                    right=x_dates[len(x_dates) - 1] + np.float64(3600*time_unit))

pyplot.plot_date(temp_xs, temp_ys, linestyle='-',
                     linewidth=1, marker=None, label='Temperature [°C]')

pyplot.plot_date(hum_xs, hum_ys, linestyle='-',
                     linewidth=1, marker=None, label='Humidity [%]')
pyplot.legend()
pyplot.title("Last Week's Data Collected")
pyplot.ylabel('Registered values')
pyplot.grid(True)
pyplot.xticks(rotation=15)

pyplot.show()
