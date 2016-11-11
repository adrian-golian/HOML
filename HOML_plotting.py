import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(data_array, title="Heatmap"):
    """ Visualise a 2d array of numbers """

    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data_array, cmap=plt.cm.Blues)
    
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_title(title)

    plt.show()