from matplotlib import pyplot
from matplotlib import animation
from datetime import date
from utils import globals


# Global variable used for displaying once the plot's legend
global run_once
run_once = True

fig = pyplot.figure()


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
            x_coordinates.append(x)
            y_coordinates.append(int(y))

    global run_once
    pyplot.locator_params(axis='x', nbins=10)
    pyplot.plot(x_coordinates, y_coordinates, color='#000066', linestyle='-', marker='o', label='coord')
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
                                   fargs=(globals.UNIVERSAL_SENSOR, title, "Time [s]", "Temperature [grd.C]"), interval=5000)
    pyplot.show()

animate_plot()