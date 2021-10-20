import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


class Compartment():
    def __init__(self, volume, transrate_out, npoints):
        self.volume = volume
        self.transrate = transrate_out
        self.quantity = np.empty((npoints,))

    @property
    def concentration(self):
        return (self.quantity / self.volume)
 
# Options
refcmpts = [[1, 1, 'Peripheral'], [1, 0.5, 'Main'], [1, 0.2, 'Sub']]
dose = lambda x: 1 / (1 + x ** 2)
model = 'ib'
clearance = 0.1
tmin = 0
tmax = 72
check_interval = 0.25

# Setup
npoints = int((tmax - tmin) / check_interval) + 1
times = np.linspace(tmin, tmax, num=npoints)


def form_rhs_ib(maincmpt, peripherals, dose, clearance):
    """ Function factory to form the right-hand side of the PK ODE for IB model
    """

    def rhs_ib(t, q):
        perfluxes = [(q[0] / maincmpt.volume - q[c+1] / p.volume)
            * p.transrate for c, p in enumerate(peripherals)]

        qcdot = np.array([dose(t) - q[0] / maincmpt.volume * clearance - sum(perfluxes)])

        qidot = np.array(perfluxes)

        return np.hstack((qcdot, qidot))

    return rhs_ib


def form_rhs_sc(subcmpt, maincmpt, peripherals, dose, clearance):
    """ Function factory to form the right-hand side of the PK ODE for SC model
    """

    def rhs_sc(t, q):
        perfluxes = [(q[1] / maincmpt.volume - q[c+2] / p.volume)
            * p.transrate for c, p in enumerate(peripherals)]

        q0dot = dose(t) - subcmpt.transrate * q[0]

        qcdot = subcmpt.transrate * q[0] - clearance * q[1] / maincmpt.volume - sum(perfluxes)

        qidot = np.array(perfluxes)

        return np.array([q0dot, qcdot, qidot])

    return rhs_sc

if __name__ == '__main__':

    peripherals = [] # List for peripheral compartments
    # Iterates through compartments. Adds peripherals to peripheral list, creates a main
    # and optionally sub compartment (if in SC model). Doesn't allow multiple main/sub
    # compartments.
    for cmpt in refcmpts:
        if cmpt[2] == 'Peripheral':
            peripherals.append(Compartment(cmpt[0], cmpt[1], npoints))
        elif cmpt[2] == 'Main':
            if 'maincmpt' in locals():
                raise ValueError("Can't have two main compartments")
            else:
                maincmpt = Compartment(cmpt[0], cmpt[1], npoints)
        elif cmpt[2] == 'Sub' and model == 'sc':
            if 'subcmpt' in locals():
                raise ValueError("Can't have two subcompartments.")
            else:
                subcmpt = Compartment(cmpt[0], cmpt[1], npoints)

    if model == 'sc':
        # Form the SC RHS and solve the ODE.
        dqdt = form_rhs_sc(subcmpt, maincmpt, peripherals, dose, clearance)
        soln = solve_ivp(dqdt, [tmin, tmax], np.zeros(len(peripherals)+2), t_eval=times)

        # This is currently broken, but it should allocate each part of the solution to its compartment.
        for c, q in enumerate(soln.y):
            if c == 0:
                subcmpt.quantity[:] = q
            elif c == 1:
                maincmpt.quantity[:] = q
            else:
                peripherals[c-2].quantity[:] = q


    if model == 'ib':
        # Form the IB RHS and solve the ODE.
        dqdt = form_rhs_ib(maincmpt, peripherals, dose, clearance)
        soln = solve_ivp(dqdt, [tmin, tmax], np.zeros(len(peripherals)+1), t_eval=times)

        # This is currently broken, but it should allocate each part of the solution to its compartment.
        for c, q in enumerate(soln.y):
            if c == 0:
                maincmpt.quantity[:] = q
            else:
                peripherals[c-1].quantity[:] = q

    pass
