#!/usr/bin/python3
from datetime import datetime


# returns the current value that sensor indicates
def current_sensor_value(sensor_data_file):
    value = -1
    try:
        file = open(sensor_data_file, 'r')
        data = file.read()
    except FileNotFoundError:
        file = open(sensor_data_file, 'x')
        data = open(sensor_data_file, 'r').read()
    values = data.split('\n')
    for coord in values:
        if len(coord) > 1:
            x, value = coord.split(",")
    file.close()
    return value


# Receives a timestring format %H:%M:%S and returns its value in seconds
def clock_time_to_seconds(clock_time):
    hrs, mins, sec = clock_time.split(":")
    return 3600*int(hrs) + 60*int(mins) + int(sec)


# timer for checking the sensor status
timer = 3  # 3 seconds


# returns a boolean if sensor is ON or OFF
def sensor_status(sensor_data_file):
    #  Set the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    time_in_sec = clock_time_to_seconds(current_time)

    # Get the data from sensor files
    data = open(sensor_data_file, 'r').read()
    lines = data.split("\n")
    if len(lines) > 0:
        coord = lines[len(lines) - 1]
        if len(coord) > 1:
            data_time, y_vals = coord.split(",")
            data_time_in_sec = clock_time_to_seconds(data_time)
            if 'None' in coord:
                return False  # Sensor is OFF
            elif time_in_sec - data_time_in_sec > timer:
                return False
            else:
                return True  # Sensor is ON
        else:
            coord = lines[len(lines) - 2]
            data_time, y_vals = coord.split(",")
            data_time_in_sec = clock_time_to_seconds(data_time)
            if 'None' in coord:
                return False
            elif time_in_sec - data_time_in_sec > timer:
                return False
            else:
                return True