import json
from sympy import DiracDelta
import numpy as np


class Dose():
    """Dose describes a generic dosing protocol.

    Protocol has a number of applications (one unless repeated dosage),
    and a time between applications.

    :param num_applications: Number of applications of the drug
    :type num_applications: int
    :param interval: Time applications given over.
    :type interval: float
    """
    def __init__(self, num_applications, interval):
        self.reps = num_applications
        self.totaltime = interval


class InstantDose(Dose):
    """InstantDose describes a single instant dose.

    Inherits from Dose.

    :param num_applications: Number of applications of the drug
    :type num_applications: int
    :param interval: Time applications given over.
    :type interval: float
    :param mass: Mass of the drug to apply (ng)
    :type mass: float
    """
    def __init__(self, num_applications, interval, mass):
        super().__init__(num_applications, interval)
        self.mass = mass

    def construct(self):
        if self.reps > 1 and self.reps.is_integer():
            apply_times = np.linspace(0, self.totaltime, self.reps)
        elif self.reps == 1:
            apply_times = np.array([0])
        else:
            raise ValueError('Number of applications must be a positive integer.')

        def protocol(t):
            
            for t0 in apply_times:

                if abs(t-t0) < (1 / 120) and (t < 1/60):
                    dose = self.mass * 60

                elif abs(t-t0) < 1/120:
                    dose = self.mass * 60

                else:
                    dose = 0

            return dose

        return protocol

class ConstantDose(Dose):
    """ConstantDose describes a dose with constant application rate.

    Inherits from Dose.

    :param num_applications: Number of applications of the drug
    :type num_applications: int
    :param interval: Time applications given over.
    :type interval: float
    :param rate: Rate of drug application (ng/hr)
    :type rate: float
    """
    def __init__(self, num_applications, interval, rate):
        super().__init__(num_applications, interval)
        self.rate = rate

    def construct(self):

        def protocol(t):
            return self.rate

        return protocol


def build_dose(filename):

    jsonfile = open(filename,)
    pdict = json.load(jsonfile)
    jsonfile.close()

    if pdict['dose_type'] == 'c':
        doseprotocol = ConstantDose(1, 0, pdict['dose'])

    elif pdict['dose_type'] == 'i':
        doseprotocol = InstantDose(1, 0, pdict['dose_mass'])

    elif pdict['dose_type'] == 'r':
        doseprotocol = InstantDose(pdict['num_dose'], pdict['time_dose'],
                                   pdict['dose_mass'])

    return doseprotocol.construct()
