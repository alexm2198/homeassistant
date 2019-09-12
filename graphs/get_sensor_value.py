#!/usr/bin/python3
import time
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


# returns a boolean if sensor is ON or OFF
def sensor_status(sensor_data_file):
    data = open(sensor_data_file, 'r').read()
    lines = data.split("\n")
    if len(lines) > 0:
        coord = lines[len(lines) - 1]
        if len(coord) > 1:
            if 'None' in coord:
                return False  # Sensor is OFF
            else:
                return True  # Sensor is ON
        else:
            coord = lines[len(lines) - 2]
            if 'None' in coord:
                return False
            else:
                return True