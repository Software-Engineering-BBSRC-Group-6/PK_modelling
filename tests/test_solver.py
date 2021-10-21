import numpy.testing as npt

from definitions import Compartment, form_rhs_ib
from solver import calc_dose

print("Running some unit tests")

# @pytest.mark.parametrize(
#     "test, expected,raise",
#     ([[1, 1, 100], [1], None]),
#     ([[-1, 1, 100], [-1], ValueError]),
# )


def test_class():
    print("Testing class initialisation")
    t = Compartment(1, 1, 100)
    assert t.volume == 1
    assert t.transrate == 1
    npt.assert_almost_equal(t.quantity/t.volume, t.concentration, decimal=2)


def test_form_rhs_ib():
    maincpt = [1, 0.5, 'Main']
    periph = [[1, 1, 'Peripheral'], 0.5, 0.5, 'Peripheral']

    form_rhs_ib(maincpt, periph, calc_dose(2), 0.1)
    assert callable(form_rhs_ib)
