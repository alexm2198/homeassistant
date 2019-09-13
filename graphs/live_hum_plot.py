from matplotlib import pyplot, dates
from matplotlib import animation
from datetime import date, datetime
from utils import globals
import numpy as np
from graphs import get_sensor_value


# Global variable used for displaying once the plot's legend
global run_once
run_once = True

# !!! TIME INTERVAL FOR PLOTTING: 1 sec = 0.00001157 time units
time_unit = 0.00001157

fig = pyplot.figure(figsize=(10, 7))
# format for X -axis displaying only hours and minutes
myFormat = dates.DateFormatter('%H:%M:%S')

def data_extractor(i, path_to_data_file, graph_title, x_label, y_label):
    try:
        data_in = open(path_to_data_file, 'r').read()
    except FileNotFoundError:
        open(path_to_data_file, 'x')
        data_in = open(path_to_data_file, 'r').read()
    x_coordinates = []
    y_coordinates = []
    lines = data_in.split("\n")
    for coord in lines:
        if len(coord) > 1:
            x, y = coord.split(",")
            if y != 'None':
                x_coordinates.append(datetime.strptime(x, '%H:%M:%S'))
                y_coordinates.append(float(y))

    global run_once
    ax = pyplot.subplot()
    ax.set_ylim([min(y_coordinates)-1, max(y_coordinates)+1])
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(myFormat)
    x_dates = dates.date2num(x_coordinates)
    if get_sensor_value.sensor_status(globals.HUM_SENSOR):
        ax.set_xlim(left=x_dates[len(x_dates)-1]-np.float64(3600*time_unit),
                    right=x_dates[len(x_dates)-1]+np.float64(600*time_unit))
    pyplot.plot_date(x_coordinates, y_coordinates, color='#43B0B7', linestyle='-',
                     linewidth=1, marker=None, label='Humidity [%]')
    if run_once:
        pyplot.legend()
        run_once = False
    pyplot.title(graph_title)
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.grid(True)


def animate_plot():
    title = date.today().strftime("%d/%m/%Y")
    anim = animation.FuncAnimation(fig, data_extractor,
                                   fargs=(globals.HUM_SENSOR, title, "Time [H:M:S]", "Humidity [%]"),
                                   interval=3000)
    pyplot.show()

animate_plot()