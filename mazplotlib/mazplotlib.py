"""
MazPlotLib
Copyright 2018 : Antoine Mazuyer
Licence: BSD 3-Clause License
"""

###############################
from tools import *
import matplotlib.pyplot as plt
###############################

def scatter(file_path, x_column=0, delimiter=None, column_title=True):
    """
    Draw a scatter plot

    Scatter is done using a CSV style file

    Parameters
    ----------
    file_path : str
        Path to the CSV style file
    x_column : int
        Position of the x column in the CVS style file
    delimiter : str
        The delimiter of the column
    column_title : bool
        Tells whether the columns have a title or not.
    """
    column_titles, columns = csv_style_file_reader(file_path, delimiter, column_title);
    nb_columns = len(columns)

    fig, ax = plt.subplots()
    print column_titles
    for i in range(nb_columns):
        if i != x_column:
            ax.plot(columns[x_column],columns[i],label=column_titles[i])
    legend = ax.legend()
    plt.show()
