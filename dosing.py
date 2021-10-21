class Dose():
    """Dose describes a generic dosing protocol.

    Protocol has a number of applications (one unless repeated dosage),
    and a time between applications.

    :param num_applications: Number of applications of the drug
    :type num_applications: int
    :param interval: Time between applications of the drug
    :type interval: float
    """
    def __init__(self, num_applications, interval):
        self.reps = num_applications
        self.period = interval


class InstantDose(Dose):
    """InstantDose describes a single instant dose.

    Inherits from Dose.

    :param num_applications: Number of applications of the drug
    :type num_applications: int
    :param interval: Time between applications of the drug
    :type interval: float
    :param mass: Mass of the drug to apply (ng)
    :type mass: float
    """
    def __init__(self, num_applications, interval, mass):
        Dose.__init__.super(self, num_applications, interval)
        self.mass = mass


class ConstantDose(Dose):
    """ConstantDose describes a dose with constant application rate.

    Inherits from Dose.

    :param num_applications: Number of applications of the drug
    :type num_applications: int
    :param interval: Time between applications of the drug
    :type interval: float
    :param rate: Rate of drug application (ng/hr)
    :type rate: float 
    """
    def __init__(self, num_applications, interval, rate):
        Dose.__init__.super(self, num_applications, interval)
        self.rate = rate

def build_dose():