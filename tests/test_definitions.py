from pk_model.definitions import Compartment, form_rhs_ib, form_rhs_sc
import numpy as np
import pytest

print("Running some unit tests")

def test_class():
    print("Testing class initialisation")
    t = Compartment(1, 1)
    assert t.volume == 1
    assert t.transrate == 1


# unit tests for form_rhs_ib
@pytest.mark.parametrize('test_input, expected, raises',
    [([[1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']]], None, None)
    ([[1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Main']]], None, AssertionError),
    ([['a string', 0.5, 'Main'], [1, 1, 'Peripheral']], None, TypeError),
    ([[1, 0.5, 'Main'], [1, 'a string', 'Peripheral']], None, TypeError)
    ]
)
def test_form_rhs_ib(test_input, expected, raises):
    if raises:
        with pytest.raises(raises):
            assert form_rhs_ib(test_input) == expected
    else:
        assert form_rhs_ib(test_input) == expected


# unit test for form_rhs_sc

@pytest.mark.parametrize('test_input, expected, raises',
    [([[0.5, 0.2, 'Sub'], [1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']]], None, None)
    ([[1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Main']]], None, AssertionError),
    ([['a string', 0.5, 'Sub'], [1, 1, 'Main']], None, TypeError),
    ([[1, 0.5, 'Sub'], [1, 'a string', 'Main']], None, TypeError)
    ]
)
def test_form_rhs_sc(test_input, expected, raises):
    if raises:
        with pytest.raises(raises):
            assert form_rhs_sc(test_input) == expected
    else:
        assert form_rhs_sc(test_input) == expected
