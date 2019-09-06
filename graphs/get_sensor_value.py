from datetime import date


# path to the file that contains the values send by the sensor in this day
global UNIVERSAL_SENSOR
UNIVERSAL_SENSOR = 'data/universal/universal_data_'+date.today().strftime("%d-%m-%Y")+".txt"



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


# Decorator for static_vars
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


# Determines if the sensor is sending data or not
global counter
counter = 2
@static_vars(file_check='data/empty.txt')
@static_vars(file='data/empty.txt')
def sensor_status(sensor_data_file):
    global counter
    if counter % 2 == 0:
        sensor_status.file_check = open(sensor_data_file).read()
        counter = 0
    if counter % 2 == 1:
        sensor_status.file = open(sensor_data_file).read()
    counter += 1
    if sensor_status.file == sensor_status.file_check:
        return False
    else:
        return True  # Sensor sends data