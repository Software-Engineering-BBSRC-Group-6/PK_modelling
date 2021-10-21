# USER INTERFACE SCRIPT
#
# This script runs the user through a series of questions
# and then returns a json with the answers to be solved
import json
import time


def user_input():
    """
    This requests user input via the command line, and then returns the requrested arguments in a dictionary

    Variables:
    model_type: Decides which model is build. This should return either intravenous bolous, subcutaenous or both
    compound: Allows the user to specify what the compound is. Useful for reporting back and for ease of understanding
    dose: Dose of compound used in ng per hour
    len_assay: Length of time should the simulation be computed across in hours
    len_interval: Granularity of time series in hours
    clearance: Time for drug to clear the system in hours
    compartments: A list of lists containing the desired compartments
    vis: Specifies if the user wants a graph generated or just a table output

    """
    print("Hello! This script builds a pharmacokinetic model.")
    model_type = input("What kind of models do you want to build? (intravenous bolous (ib) / subcutaneous (sc))")
    compound = input("What compound or drug are you using?")
    dose_type = input("How is the dose delivered? Constantly over time (c), Instantaneously (i) or Repeated instantaneous doses (r)")

    if dose_type == 'c':
        dose =  input("What is the dose of " + compound + " that you want to test? (units in ng per hour)")
        dose_mass = None
        time_dose = None
        num_dose = None
    elif dose_type == 'i':
        dose_mass =  input("What is the mass of the dose of " + compound + " that you want to test? (units in ng)")
        dose = None
        time_dose = None
        num_dose = None
    elif dose_type == 'r':
        dose_mass =  input("What is the mass of the dose of " + compound + " that you want to test? (units in ng)")
        time_dose = input("What time period are the doses given over? (units in hours")
        num_dose = input("How many doses are given? - this program assumes that doses are evenly spaced throughout the time period.")
        dose = None

    len_assay = input("Assay time? (units in hours)")
    len_interval = input("What interval time would you like? (units in hours)")
    clearance = input("What is the clearance time? (units in hours)")

    compartments = []

    if model_type == "ib":

        main_compart = input("Enter volume (L), transition rate () for the main compartment (all seperated by spaces - eg: 5 25 )")
        main_compart_split = main_compart.split()
        main_compart_split.append(str("Main"))
        compartments.append(main_compart_split)

        num_peripherals = input("How many peripheral compartments do you want to test?")

        num_peripherals = int(num_peripherals)

        if num_peripherals > 0:

            for i in range(num_peripherals):
                compart = input("Enter volume (L), transition rate (), name of compartment (all seperated by spaces - eg: 5 25 upper-lung)")
                compart_list = compart.split()
                compartments.append(compart_list)

    elif model_type == "sc":

        sub_compart = input("Enter volume (L), transition rate () for the sub compartment (all seperated by spaces - eg: 5 25 )")
        sub_compart_split = sub_compart.split()
        sub_compart_split.append(str("Sub"))
        compartments.append(sub_compart_split)

        main_compart = input("Enter volume (L), transition rate () for the main compartment (all seperated by spaces - eg: 5 25 )")
        main_compart_split = main_compart.split()
        main_compart_split.append(str("Main"))
        compartments.append(main_compart_split)

        num_peripherals = input("How many peripheral compartments do you want to test?")
        num_peripherals = int(num_peripherals)

        if num_peripherals > 0:

            for i in range(num_peripherals):
                compart = input("Enter volume (L), transition rate (), name of compartment (all seperated by spaces - eg: 5 25 upper-lung)")
                compart_list = compart.split()
                compartments.append(compart_list)


    vis = input("Would you like to generate a graph? (Y/N)")

    curr_datetime = time.time()
    curr_datetime = str(curr_datetime)


    print("Thank you! Building model, please wait...")


    return {
        'model_type': model_type,
        'compound': compound,
        'dose_type': dose_type,
        'dose':dose,
        'dose_mass': dose_mass,
        'time_dose': time_dose,
        'num_dose': num_dose,
        'len_assay':len_assay,
        'len_interval':len_interval,
        'clearance':clearance,
        'compartments':compartments,
        'vis':vis,
        'curr_datetime':curr_datetime
        }

def param_to_file():
    """
    Writes dictionary generated from user_input() and generates .json file
    """
    data = user_input()
    fname = data.get('curr_datetime')
    f = open(fname+".json", "w")
    json.dump(data, f)
    f.close()
    filename = fname+".json"

    return filename


def num_models():
    """
    Defines how many modeles will be tested
    """
    N = input("How many models would you like to test?")
    N = int(N)
    return N


if __name__ == "__main__":
    N = num_models()
    for i in range(N):
        param_to_file()
