# USER INTERFACE SCRIPT
# 
# This script runs the user through a series of questions
# and then returns a dictionary with the answers to be solved
import json

def user_input():
    """
    This requests user input via the command line, and then returns the requrested arguments in a dictionary

    Variables:
    len_model_type: How many models should be created? This should be an interger between 1 and 3
    model_type: Decides which model is build. This should return either intravenous bolous, subcutaenous or both
    compound: Allows the user to specify what the compound is. Useful for reporting back and for ease of understanding
    dose: Dose of compound used in ng per hour
    len_assay: Length of time should the simulation be computed across in hours
    len_interval: Granularity of time series in hours
    clearance: Time for drug to clear the system in hours
    len_compartments: Specifies number of compartments in the model
    compartments: A list of lists containing the desired compartments
    vis: Specifies if the user wants a graph generated or just a table output

    """
    print("Hello! This script builds a pharmacokinetic model.")
    len_model_type = input("How many models do you want to build?")
    model_type = input("What kind of models do you want to build? (intravenous bolous / subcutaenous / both)")
    compound = input("What compound or drug are you using?")
    dose =  input("What is the dose of " + compound + " that you want to test? (units in ng per hour)")
    len_assay = input("Assay time? (units in hours)")
    len_interval = input("What interval time would you like? (units in hours)")
    clearance = input("What is the clearance time? (units in hours)")
    len_compartments = input("How many compartments do you want to test?")
    len_compartments = int(len_compartments)

    compartments = []

    for i in range(len_compartments):
        compart = input("Enter volume (L), transition rate (), name of compartment and type of compartment (all seperated by spaces - eg: 5 25 upper-lung main)")
        compart_list = compart.split()
        compartments.append(compart_list)

    vis = input("Would you like to generate a graph? (Y/N)")

    print("Thank you! Building model, please wait...")

    return {
        'len_model_type': len_model_type, 
        'model_type': model_type, 
        'compound': compound, 
        'dose':dose, 
        'len_assay':len_assay, 
        'len_interval':len_interval, 
        'clearance':clearance, 
        'len_compartments':len_compartments, 
        'compartments':compartments, 
        'vis':vis
        }

def param_to_file():
    """
    Writes dictionary generated from user_input() and generates .json file
    """
    f = open("param.json", "w")
    json.dump(user_input(), f)
    f.close()

if __name__ == "__main__":
    param_to_file()

