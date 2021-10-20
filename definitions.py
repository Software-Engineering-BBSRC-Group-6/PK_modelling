class Compartment():
    """ Compartment class; describes an individual compartment in either model type.
    

    """
    def __init__(self, volume, transrate_out, npoints):
        self.volume = volume
        self.transrate = transrate_out
        self.quantity = np.empty((npoints,))

    @property
    def concentration(self):
        return (self.quantity / self.volume)

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