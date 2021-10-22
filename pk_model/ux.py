# USER INTERFACE SCRIPT
#
# This script runs the user through a series of questions
# and then returns a json with the answers to be solved
import json
import time
import os


def user_input():
    """
    This requests user input via the command line, and then returns the requested arguments in a dictionary

    :param model_type: Decides which model is build. This should return either intravenous bolous, subcutaenous or both
    :type model_type: string
    :param compound: Allows the user to specify what the compound is. Useful for reporting back and for ease of understandingx
    :param dose: Dose of compound used in ng per hour
    :param len_assay: Length of time should the simulation be computed across in hours
    :param len_interval: Granularity of time series in hours
    :param clearance: Time for drug to clear the system in hours
    :param compartments: A list of lists containing the desired compartments
    :param vis: Specifies if the user wants a graph generated or just a table output
    """
    #Error messages
    num_invalid = "Invalid input, please insert a valid number"
    str_invalid = "Invalid input, please try again following the input conventions requested"

    #Model Type
    model_type = input("What kind of models do you want to build? (intravenous bolous (ib) / subcutaneous (sc)): ")
    model_type = model_type.lower()
    while model_type not in {'ib', 'sc'}:
        print(str_invalid)
        model_type = input("What kind of models do you want to build? (intravenous bolous (ib) / subcutaneous (sc)): ")
        model_type = model_type.lower()

    #Compound
    compound = input("What compound or drug are you using?")
    
    #Dose Type
    dose_type = input("How is the dose delivered? Constantly over time (c), Instantaneously (i) or Repeated instantaneous doses (r): ")
    dose_type = dose_type.lower()
    while dose_type not in {"c","i","r"}:
        print(str_invalid)
        dose_type = input("How is the dose delivered? Constantly over time (c), Instantaneously (i) or Repeated instantaneous doses (r): ")
        dose_type = dose_type.lower()

    if dose_type == 'c':
        while True:
            try:
                dose =  float(input("What is the dose of " + compound + " that you want to test? (units in ng per hour): "))
                break
            except:
                print(num_invalid)
        dose_mass = None
        time_dose = None
        num_dose = None
        
    elif dose_type == 'i':
        while True:
            try:
                dose_mass =  float(input("What is the mass of the dose of " + compound + " that you want to test? (units in ng): "))
                break
            except:
                print(num_invalid)
        dose = None
        time_dose = None
        num_dose = None

    elif dose_type == 'r':
        while True:
            try:
                dose_mass =  float(input("What is the mass of the dose of " + compound + " that you want to test? (units in ng): "))
                break
            except:
                print(num_invalid)
        while True:
            try:
                time_dose = float(input("What time period are the doses given over? (units in hours): "))
                break
            except:
                print(num_invalid)
        while True:
            try:
                num_dose = float(input("How many doses are given? - this program assumes that doses are evenly spaced throughout the time period: "))
                break
            except:
                print(num_invalid)
        dose = None
    
    #Length of simulation time
    while True:
        try:
            len_assay = float(input("What time period would you like to simluate the model? (units in hours): "))
            break
        except:
	        print(num_invalid)
    
    #Interval times
    while True:
        try:
            len_interval = float(input("What interval time would you like in the simulation? (units in hours): "))
            break
        except:
            print(num_invalid)

    #clearance
    while True:
        try:
            clearance = float(input("What is the clearance rate? (units in ng/hour): "))
            break
        except:
            print(num_invalid)

    
    #compartments
    compartments = []

    if model_type == "ib":
        while True:
            try:
                main_compart = input("Enter volume (L), transition rate (ng/hour) for the main compartment (all seperated by spaces - eg: 5 25 ): ")
                main_compart_split = main_compart.split()
                main_compart_split = [float(i) for i in main_compart_split]
                break
            except:
                print(str_invalid)

        main_compart_split.append(str("Main"))
        compartments.append(main_compart_split)


        while True:
            try:
                num_peripherals = float(input("How many peripheral compartments do you want to test?: "))
                break
            except:
	            print(num_invalid)

        num_peripherals = int(num_peripherals)

        if num_peripherals > 0:
            
            for i in range(num_peripherals):
                while True:
                    try:
                        compart = input("Enter volume (L), transition rate (ng/hour) of the compartment (all seperated by spaces - eg: 5 25): ")
                        compart_list = compart.split()
                        compart_list = [float(i) for i in compart_list]
                        break
                    
                    except:
                        print(str_invalid)

                compart.list.append((str("Perf")))
                compart_list.append(str(input("Please enter the name of the compartment (please ensure correct spelling): ")))
                compartments.append(compart_list)

                compart_list = None
    
    elif model_type == "sc":
        while True:
            try:
                sub_compart = input("Enter volume (L), transition rate (ng/hour) for the sub compartment (all seperated by spaces - eg: 5 25 ): ")
                sub_compart_split = sub_compart.split()
                sub_compart_split = [float(i) for i in sub_compart_split]
                break
            except:
                print(str_invalid)

        sub_compart_split.append(str("Sub"))
        compartments.append(sub_compart_split)

        while True:
            try:
                main_compart = input("Enter volume (L), transition rate (ng/hour) for the main compartment (all seperated by spaces - eg: 5 25 ): ")
                main_compart_split = main_compart.split()
                main_compart_split = [float(i) for i in main_compart_split]
                break

            except:
                print(str_invalid)

        main_compart_split.append(str("Main"))
        compartments.append(main_compart_split)

        while True:
            try:
                num_peripherals = float(input("How many peripheral compartments do you want to test?: "))
                break
            except:
	            print(num_invalid)
        
        num_peripherals = int(num_peripherals)

        if num_peripherals > 0:
            
            for i in range(num_peripherals):
                while True:
                    try:
                        compart = input("Enter volume (L), transition rate (ng/hour) of the compartment (all seperated by spaces - eg: 5 25): ")
                        compart_list = compart.split()
                        compart_list = [float(i) for i in compart_list]
                        break
                    
                    except:
                        print(str_invalid)
                
                compart.list.append((str("Perf")))
                compart_list.append(str(input("Please enter the name of the compartment (please ensure correct spelling): ")))
                compartments.append(compart_list)
                compart_list = None

    #visualisation
    vis = input("Would you like to generate a graph? (Y/N): ")
    while vis not in {'Y','y','N','n'}:
        print(str_invalid)
        vis = input("Would you like to generate a graph? (Y/N): ") 

    #unix timestamp
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
    fname = 'jsons/' + data.get('curr_datetime') + '.json'
    f = open(fname , 'w')
    json.dump(data, f)
    f.close()

    return fname


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
