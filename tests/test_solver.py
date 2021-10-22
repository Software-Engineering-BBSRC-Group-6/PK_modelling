from definitions import Compartment, form_rhs_ib
from solver import calc_dose, generate_times
import numpy as np
import pytest

print("Running some unit tests")


def test_class():
    print("Testing class initialisation")
    t = Compartment(1, 1)
    assert t.volume == 1
    assert t.transrate == 1


@pytest.mark.parametrize('test_input, expected, raises',
    [([5, 0.5], np.linspace(0, 5, num=int(5/0.5 + 1)), None),
     ([5, 'a string'], None, ValueError),
     (['a string', 0.5], None, ValueError),
     ([5, 0], None, ValueError),
     ([0, 5], None, ValueError),
    ]
)
def test_generate_times(tmax, check_interval):
    generate_times(tmax, check_interval)


@pytest.mark.parametrize('test_input, expected, raises',
    [([1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']], None , None),
    ]
)
def test_form_rhs_ib(maincmpt, periph):

    form_rhs_ib(maincmpt, periph, calc_dose(2), 0.1)
    assert callable(form_rhs_ib)
