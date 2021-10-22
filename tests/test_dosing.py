from definitions import Compartment, form_rhs_ib
from dosing import Dose, InstantDose, ConstantDose, build_dose
import numpy as np

print("Running some unit tests on dosing")

def test_dose():
    d = Dose(1,1.0)
    assert d.reps == 1
    assert d.totaltime == 1.0

def test_instant_dose():
    idose = InstantDose(1, 1.0, 1.0)
    assert idose.mass == 1.0
    assert idose.construct == np.linspace(0, 1.0, 1.0)


def test_constant_dose():
    cdose = ConstantDose(1, 1.0, 1.0)
    assert cdose.rate == 1.0
    assert cdose.construct == 1.0

def test_build_dose():
    
