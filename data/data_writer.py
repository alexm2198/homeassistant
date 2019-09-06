import random
import time
from datetime import date, datetime


# Random generator of values. Each value is generated in a delta t = 1 second and in (0,30) range.
def data_writer(file_to_write):
    try:
        open(file_to_write, 'r')
    except FileNotFoundError:
        open(file_to_write, 'x')
    while True:
        time_axis = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
        data_to_write = str(random.randint(0, 50))
        open(file_to_write, "a").write(f'{time_axis},{data_to_write}\n')
        time.sleep(1)


data_writer('universal/universal_data_' + date.today().strftime("%d-%m-%Y") + '.txt')