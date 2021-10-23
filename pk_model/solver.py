import numpy as np
from scipy.integrate import solve_ivp
from pk_model.definitions import Compartment, form_rhs_ib, form_rhs_sc, write_solution_file
import json

# Some old sample options -
# to be removed, updated and included in some kind of unit test instead.


def generate_times(tmax, check_interval):
    """Generates an array of times to be checked by the solver.

    :param tmin: Time of start of assay (hours)
    :type tmin: float
    :param tmax: Time of end of assay (hours)
    :type tmax: float
    :param check_interval: Time interval between data points (hours).
    :type check_interval: float

    :return times: Contains the times at which data points are wanted from the solver.
    :type times: numpy array
    """
    if check_interval == 0:
        raise ValueError('Cannot divide by zero.')
    elif tmax == 0:
        raise ValueError('Assay cannot last zero time.')
    elif not (tmax / check_interval).is_integer():
        raise ValueError('Must be able to output an integer number of times.')
    npoints = int(tmax / check_interval) + 1
    times = np.linspace(0, tmax, num=npoints)
    return times


def generate_compartments(parameterdict):
    """Turns a list of compartment parameters into a set of compartment objects.

    :param parameterdict: Dictionary containing a list with key 'compartments', formatted as [Volume Transition Rate Type Name], and a second key 'model_type' which is either 'ib' or 'sc'.
    :type parameterdict: dictionary
    """

    refcmpts = parameterdict['compartments']
    model = parameterdict['model_type']

    peripherals = []  # List for peripheral compartments
    # Iterates through compartments. Adds peripherals to peripheral list,
    # creates main and optionally sub compartment (if in SC model).
    # Doesn't allow multiple main/sub compartments.
    for cmpt in refcmpts:
        if cmpt[2] == 'Peripheral':
            peripherals.append(Compartment(cmpt[0], cmpt[1]))

        elif cmpt[2] == 'Main':
            if 'maincmpt' in locals():
                raise ValueError("Can't have two main compartments.")
            else:
                maincmpt = Compartment(cmpt[0], cmpt[1])

        elif cmpt[2] == 'Sub' and model == 'sc':
            if 'subcmpt' in locals():
                raise ValueError("Can't have two subcompartments.")
            else:
                subcmpt = Compartment(cmpt[0], cmpt[1])

    if 'subcmpt' not in locals():
        subcmpt = None

    return maincmpt, peripherals, subcmpt


def get_solution(model, subcmpt, maincmpt,
                 peripherals, dose, clearance, times):
    """Finds solution of drug dosage over time for a given set of compartments, dose and clearance rate

    :param model: the input model, subcutaneous (sc) or IV bolus (ib)
    :type model: string
    :param subcompt: subcompartment
    :param maincmpt: main compartment
    :param peripheral: the peripheral compartments added
    :param dose: dose function
    :param clearance: clearance rate
    :param times: time points to solve model"""

    if model == 'sc':
        # Form the SC RHS and solve the ODE.

        dqdt = form_rhs_sc(subcmpt, maincmpt, peripherals, dose, clearance)
        soln = solve_ivp(dqdt, [0, times[-1:]], np.zeros(len(peripherals)+2),
                         t_eval=times)

    elif model == 'ib':
        # Form the IB RHS and solve the ODE.

        dqdt = form_rhs_ib(maincmpt, peripherals, dose, clearance)
        soln = solve_ivp(dqdt, [0, times[-1:]],
                         np.zeros(len(peripherals)+1), t_eval=times)

    else:
        raise AssertionError("Model not recognised.")

    return soln


def build_and_solve_model(filename, dosing_function):
    """Opens a file containing model parameters, builds a model, solves it, and writes the output to file.

    :param filename: Name of .json file containing program parameters (see ux for details).
    :type filename: string
    :param dosing_function: Describes the dosing protocol as a function of time (in hours)
    :type dosing_function: function object

    :return datafile: Name of the file where the solution is stored.
    :type datafile: string
    """
    jsonfile = open(filename,)
    pdict = json.load(jsonfile)
    jsonfile.close()

    times = generate_times(pdict['len_assay'], pdict['len_interval'])
    main, periph, sub = generate_compartments(pdict)
    soln = get_solution(pdict['model_type'], sub, main, periph,
                        dosing_function, pdict['clearance'], times)

    write_solution_file(soln, pdict['model_type'], pdict['curr_datetime'])

    return './data/{0}-{1}.csv'.format(pdict['model_type'],
                                       pdict['curr_datetime'])
