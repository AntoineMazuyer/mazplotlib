"""
MazPlotLib
Copyright 2018 : Antoine Mazuyer
Licence: BSD 3-Clause License
"""

"""
This file contains some tools useful for all the plot functions
"""

def csv_style_file_reader(file_path, delimiter=None, column_title=True):
    """
    Read a csv style file and load its contents

    Parameters
    ----------
    file_path : str
        Path to the CSV style file. The CSV file can have the first line describing the content
        of the columns.
    delimiter : str
        The delimiter of the column
    column_title : bool
        Tells whether the columns have a title or not.

    Returns
    -------
    list
        List of column names
    list of list
        list of the columns
    """
    the_file = open(file_path,'r')

    # This will be return
    column_titles = []

    #Get information from the first line
    first_line = the_file.readline()
    split_line = first_line.split(delimiter)
    nb_columns = len(split_line);

    # This will be return
    columns = [ [] for i in range(nb_columns) ]
    # Explaination: https://stackoverflow.com/questions/12791501/python-initializing-a-list-of-lists

    # Transfer the line in column titles
    if column_title:
        column_titles = split_line
    else:
        column_titles = ["Column "+ str(i) for i in range(nb_columns)];
        for i in range (nb_columns):
            columns[i].append( float(split_line[i]))

    for line in the_file:
        split_line = line.split(delimiter)
        if len(split_line) != 0:
            for i in range (nb_columns):
                columns[i].append( float(split_line[i]))

    return column_titles, columns
