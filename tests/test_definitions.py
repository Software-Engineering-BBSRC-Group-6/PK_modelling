from pk_models.definitions import Compartment, form_rhs_ib, form_rhs_sc, rhs_ib, rhs_sc
import numpy as np
import pytest

print("Running some unit tests")

def test_class():
    print("Testing class initialisation")
    t = Compartment(1, 1)
    assert t.volume == 1
    assert t.transrate == 1

# unit tests for rhs_ib
@pytest.mark.parametrize('test_input, expected, raises',
    [([0, np.array(0.0, 0.0, 0.0)], 0, None),
    (['a string', np.array(1.0, 2.0, 3.0)], None, TypeError),
    ([1, np.array('a string')], None, TypeError)
    ]
)
def test_rhs_ib(test_input, expected, raises):
    if raises:
        with pytest.raises(raises):
            assert rhs_ib(test_input) == expected
    else:
        assert rhs_ib(test_input) == expected

# unit tests for form_rhs_ib
@pytest.mark.parametrize('test_input, expected, raises',
    [([1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']], None, None)
    ]
)
def test_form_rhs_ib(maincmpt, periph):
    form_rhs_ib(maincmpt, periph, calc_dose(2), 0.1)
    assert callable(form_rhs_ib)

# unit tests for rhs_sc
@pytest.mark.parametrize('test_input, expected, raises',
    [([0, np.array(0.0, 0.0, 0.0)], 0, None),
    (['a string', np.array(1.0, 2.0, 3.0)], None, TypeError),
    ([1, np.array('a string')], None, TypeError)
    ]
)
def test_rhs_sc(test_input, expected, raises):
    if raises:
        with pytest.raises(raises):
            assert rhs_sc(test_input) == expected
    else:
        assert rhs_sc(test_input) == expected

# unit test for form_rhs_ib
@pytest.mark.parametrize('test_input, expected, raises',
    [([0.5, 0.2, 'Sub'], [1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']], None , None)
    ]
)
def test_form_rhs_ib(subcmpt, maincmpt, periph):
    form_rhs_sc(subcmpt, maincmpt, periph, calc_dose(2), 0.1)
    assert callable(form_rhs_sc)
