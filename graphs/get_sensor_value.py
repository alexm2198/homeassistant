import time

# returns the current value that sensor indicates
def current_sensor_value(sensor_data_file):
    value = -1
    file = open(sensor_data_file, 'r')
    data = file.read()
    values = data.split('\n')
    for coord in values:
        if len(coord) > 1:
            x, value = coord.split(",")
    file.close()
    return value


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


global counter
counter = 2
@static_vars(file_check=open('data/data1_in.txt').read())
@static_vars(file=open('data/data1_in.txt').read())
def sensor_status():
    global counter
    if counter % 2 == 0:
        sensor_status.file_check = open('data/data1_in.txt').read()
        counter = 0
    if counter % 2 == 1:
        sensor_status.file = open('data/data1_in.txt').read()
    counter += 1
    if sensor_status.file == sensor_status.file_check:
        return False
    else:
        return True  # Sensor sends data