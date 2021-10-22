import unittest
from pk_model.dosing import Dose, InstantDose, ConstantDose, build_dose
import json
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
    data = {
    "model_type": "ib", 
    "compound": "paracetamol", 
    "dose_type": "c", 
    "dose": 0.5, 
    "dose_mass": None, 
    "time_dose": None, 
    "num_dose": None, 
    "len_assay": 72.0, 
    "len_interval": 0.25, 
    "clearance": 0.4, 
    "compartments": [[1.0, 0.3, "Main"], [0.5, 0.15, "Heart"]], 
    "vis": "y", 
    "curr_datetime": "1634833362.6048021"}

    f = 'dummy.json'
    f = open(f , 'w')
    dummy = json.dump(data, f)
    f.close()

    test = build_dose("dummy.json")
    assert test == 0.5

