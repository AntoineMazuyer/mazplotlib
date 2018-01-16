"""
MazPlotLib
Copyright 2018 : Antoine Mazuyer
Licence: BSD 3-Clause License
"""

###############################
from tools import *
import matplotlib.pyplot as plt
import matplotlib
###############################

def plot(
        file_path,
        x_column=0,
        delimiter=None,
        column_title=True,
        display_legend=False,
        x_label = "",
        y_label = "",
        font_size = 22,
        line_width = 5,
        plot_style = "seaborn-whitegrid"):
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
    display_legend : bool
        Tells wether the legend of the plots should be displayed or not
    x_label : str
        Label of the X axis
    y_label : str
        Label of the Y axis
    font_size : int
        Size of the fonts
    line_width : int
        Width of the line
    plot_style : str
        Plot style available form matplotlib
    """
    plt.style.use(plot_style)
    matplotlib.rcParams.update({'font.size': font_size})
    column_titles, columns = csv_style_file_reader(file_path, delimiter, column_title);
    nb_columns = len(columns)

    fig, ax = plt.subplots()
    for i in range(nb_columns):
        if i != x_column:
            ax.plot(columns[x_column],columns[i],label=column_titles[i], linewidth=line_width)
    if display_legend:
        legend = ax.legend(facecolor='w',fancybox=True,frameon=True)
    plt.xlabel(x_label) 
    plt.ylabel(y_label) 
    plt.show()
