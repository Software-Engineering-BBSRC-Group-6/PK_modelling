import numpy as np 
import matplotlib.pyplot as plt
import csv
import json

"""
JSON Format
return {
        'model_type': model_type,
        'compound': compound,
        'dose':dose,
        'len_assay':len_assay,
        'len_interval':len_interval,
        'clearance':clearance,
        'compartments':compartments,
        'vis':vis
        }
"""

# Load single JSON file and return data for plotting
def single_plot_data(json_file, csv_file):
    '''
    Read parameters and data from models to generate a list of model parameters, data array and its dimensions
    
    :param json_file: Name of the json file to be opened
    :type json_file: string
    :param csv_file: Name of the csv file to be opened
    :type csv_file: string
    :return plot_value: list containing [parameters, data_array, num_rows, num_columns]
    '''
    # Empty list to be returned
    plot_values = []
    # Open JSON file
    json_fileobj = open(json_file,)
    # Return JSON file as dictionary
    param_dict = json.load(json_fileobj)
    plot_values.append(param_dict)
    # Create array from data with columns as data lists (e.g. time first column)
    data_array = np.loadtxt(csv_file, delimiter=",")
    plot_values.append(data_array)
    # Obtain number of columns
    num_rows, num_cols = list(data_array.shape)[0], list(data_array.shape)[1]
    plot_values.append(num_rows)
    plot_values.append(num_cols)
    
    return plot_values

# Run is list formatted as [[json1, csv1], [json2, csv2]...] 
def collate_data(run):
    '''
    Collate the lists returned by single_plot to return a list of lists for all simulations
    in a run
    :param run: list formatted as [[json1.json, csv1.csv], [json2.json, csv2.csv]...]
    :return collated_list: matrix containing data matrices for all simulations
    '''
    # Create collated list
    collated_list = []
    # Append data from each simulation
    for i in run:
        collated_list.append(single_plot_data(i[0], i[1]))
    return collated_list

# Plot data from collated data structure
def multiplot(collated_list):
    '''
    Plot overlayed simulation data from multiple runs using collated data matrix
    :param collated_list: matrix containing data matrices for all simulations
    :return: display overlayed plots for each compartment
    '''
    # Iterate over simulations to obtain maximum compartment number
    comp_list = []
    for i in collated_list:
        comp_list.append(i[3])
    compartments = max(comp_list) - 1

    # Set up sub plot 
    fig, axs = plt.subplots(1, compartments)

    # Iterate over simulation data
    for i in range(len(collated_list)):
        for j in range(compartments):
            # Collated list indices as collated_list[index simulation][index plot_values][index data type]
            axs[j].plot(collated_list[0][1][:,0], collated_list[i][1][:,j+1])
            axs[j].set_title(str(collated_list[0][0]['compartments'][j][2]))
            axs[j].set(xlabel='time', ylabel='quantity')

    plt.tight_layout()
    plt.show()

def make_plots(filenames):
    """Fill me in later."""
    multiplot(collate_data(filenames))

