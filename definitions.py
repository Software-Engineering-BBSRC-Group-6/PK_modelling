import numpy as np


class Compartment():
    """ Compartment describes an individual compartment in either model type.

    :param volume: Volume of compartment
    :type volume: float
    :param transrate: Transition rate out of a given compartment
    :type transrate: float
    """

    def __init__(self, volume, transrate_out):
        self.volume = volume
        self.transrate = transrate_out
        if volume < 0:
            raise ValueError("Volume must be >= 0")


def form_rhs_ib(maincmpt, peripherals, dose, clearance):
    """Function factory to form the right-hand side of the PK ODE for IB model.

    :param maincmpt: Object corresponding to the main compartment
    :type maincmpt: compartment
    :param peripherals: List containing each peripheral compartment object
    :type peripherals: list, each listem item is Compartment.
    :param dose: Function, one argument (time), describes dosing protocol.
    :type dose: Function
    :param clearance: Clearance rate from the main compartment.
    :type clearance: float

    :return rhs_ib: RHS of the PK ODE for the IB model, taking parameters t
    (time) and an N-dimensional vector of q (floats).
    """

    def rhs_ib(t, q):
        """Returns the right-hand side of the ODE for the IB model, including
        the parameters of the various compartments.

        :param t: time
        :type t: float
        :param q: N-dimensional vector with q[0] as the main compartment and
        q[1] ... q[N-1] as the peripheral compartments.
        :type q: numpy array of floats of size (N,).

        :return dqdt: The value of the N-dimensional time derivative at time t.
        :type dqdt: numpy array of floats of size (N,).
        """
        perfluxes = [(q[0] / maincmpt.volume - q[c+1] / p.volume)
                     * p.transrate for c, p in enumerate(peripherals)]

        qcdot = np.array([dose(t) - q[0] / maincmpt.volume * clearance
                          - sum(perfluxes)])

        qidot = np.array(perfluxes)

        return np.hstack((qcdot, qidot))

    return rhs_ib


def form_rhs_sc(subcmpt, maincmpt, peripherals, dose, clearance):
    """Function factory to form the right-hand side of the PK ODE for IB model.
    :param subcmpt: Object corresponding to the subcutaneous compartment
    :type subcmpt: Compartment object
    :param maincmpt: Object corresponding to the main compartment
    :type maincmpt: Compartment object
    :param peripherals: List containing each peripheral compartment object
    :type peripherals: list, each listem item is Compartment.
    :param dose: Function, one argument (time), describes dosing protocol.
    :type dose: Function
    :param clearance: Clearance rate from the main compartment.
    :type clearance: float
    """

    def rhs_sc(t, q):
        """Returns the right-hand side of the ODE for the SC model, including
        the parameters of the various compartments.

        :param t: time
        :type t: float
        :param q: N-dimensional vector with q[0] as the sub compartment,
        q[1] as the main compartment, and q[2] ... q[N-1] as the peripheral
         compartments.
        :type q: numpy array of floats of size (N,).

        :return dqdt: The value of the N-dimensional time derivative at time t.
        :type dqdt: numpy array of floats of size (N,).
        """
        perfluxes = [(q[1] / maincmpt.volume - q[c+2] / p.volume)
                     * p.transrate for c, p in enumerate(peripherals)]

        q0dot = dose(t) - subcmpt.transrate * q[0]

        qcdot = np.array([subcmpt.transrate * q[0] - clearance * q[1]
                         / maincmpt.volume - sum(perfluxes)])

        qidot = np.array(perfluxes)

        return np.hstack((q0dot, qcdot, qidot))

    return rhs_sc


def write_solution_file(solution, model, timestamp):
    """Puts the scipy solution into a data file for reading by the visualiser.

    :param solution: solution from scipy solve_ivp().
    :type solution: bunch
    :param model: type of model, one of 'sc' or 'ib' as defined earlier by
     user.
    :type model: string
    :param timestamp: time at which the solver was run, used to identify a
     given run.
    :type timestamp:  string

    :return solutionmat: Contains timeseries data, and solutions for each
    compartment.
    :type solutionmat: Numpy array
    """

    if model == 'sc':
        solutionmat = np.hstack((solution.t[:, np.newaxis],
                                np.transpose(solution.y)))

    elif model == 'ib':
        solutionmat = np.hstack((solution.t[:, np.newaxis],
                                np.zeros((len(solution.t), 1)),
                                np.transpose(solution.y)))

    np.savetxt('./data/{0}-{1}.csv'.format(model, timestamp), solutionmat,
               delimiter=',')

    return solutionmat
