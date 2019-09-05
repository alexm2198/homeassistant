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