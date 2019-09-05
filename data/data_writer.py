import random
import time


# Random generator of values. Each value is generated in a delta t = 1 second and in (0,30) range.
def data_writer(file_to_write):
    try:
        open(file_to_write, 'r')
    except FileNotFoundError:
        open(file_to_write, 'x')
    time_passed = 0
    while True:
        data_to_write = str(random.randint(0, 50))
        open(file_to_write, "a").write(f'{time_passed},{data_to_write}\n')
        time.sleep(1)
        time_passed += 1


data_writer('data1_in.txt')