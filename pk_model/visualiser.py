import numpy as np 
import matplotlib.pyplot as plt
import csv
import json

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
    num_rows, num_cols = data_array.shape
    plot_values.append(num_rows)
    plot_values.append(num_cols)
    
    return plot_values

# Run is list formatted as [[json1, csv1], [json2, csv2]...] 
def collate_data(run):
    '''
    Collate the lists returned by single_plot to return a list of lists for all simulations in a run
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
        # Append column number of data array
        comp_list.append(i[3])
    # Account for time (not a compartment)
    compartments = max(comp_list) - 1

    # Initialise subplot space to contain compartment plots
    fig, axs = plt.subplots(1, compartments)
   
    # Iterate over simulation data
    for i in range(len(collated_list)):

        num_rows_plot, num_cols_plot = collated_list[i][1].shape

        if collated_list[i][0]["model_type"] == "ib":
            for j in range(2, num_cols_plot):
                # Collated list indexed as collated_list[index simulation][index plot_values][index data type]
                # Plot time against drug level in each compartment
                axs[j-1].plot(collated_list[i][1][:,0], collated_list[i][1][:,j], label=str(collated_list[i][0]["compound"]))
                axs[j-1].set_title("Compartment: " + str(collated_list[i][0]['compartments'][j-2][-1]))
                axs[j-1].set(xlabel='Time / hours', ylabel='Quantity / nanograms')

        elif collated_list[i][0]["model_type"] == "sc":
            for j in range(1, num_cols_plot):
                # Collated list indexed as collated_list[index simulation][index plot_values][index data type]
                # Plot time against drug level in each compartment
                axs[j-1].plot(collated_list[i][1][:,0], collated_list[i][1][:,j], label=str(collated_list[i][0]["compound"]))
                axs[j-1].set_title("Compartment: " + str(collated_list[i][0]['compartments'][j-1][-1]))
                axs[j-1].set(xlabel='Time / hours', ylabel='Quantity / nanograms')

    # Initialise list to contain model type for each simulation
    mod_array = []

    # Check if any simulations are 'sc' model type. If not - delete sub compartment plot and restructure plot space
    for i in range(len(collated_list)):
        mod_array.append(collated_list[i][0]["model_type"])

    if "sc" not in mod_array:
        # Delete first plot
        fig.delaxes(axs[0])
        # Restructure plot space
        for i in range(1, compartments):
            axs[i].change_geometry(1,compartments - 1,i)

    plt.legend()
    plt.tight_layout()
    
    # Display plot
    plt.show()
    

def make_plots(filenames):
    '''
    Combine multiplot and collate_data functions to produce overlayed plots of drug concentration against time for
    all user specified compartments.

    :param filenames: Simulation filename list formatted as [[json1, csv1], [json2, csv2]...]  
    '''

    multiplot(collate_data(filenames))

