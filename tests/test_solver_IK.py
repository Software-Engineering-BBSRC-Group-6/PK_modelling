from pk_model.definitions import Compartment, form_rhs_ib
from pk_model.solver import calc_dose, generate_times, generate_compartments, get_solution
import numpy as np
import pytest

print("Running some unit tests")

# Unit test for calc_dose
@pytest.mark.parametrize('test_input, expected, raises',
    [(3, 0.1, None),
    (0.5, 0.8, None),
    ('a string', None, TypeError)]
)
def test_calc_dose(test_input, expected, raises):
    from solver import calc_dose
    if raises:
        with pytest.raises(raises):
            assert calc_dose(test_input) == expected
    else:
        assert calc_dose(test_input) == expected

#unit test for generate_time
@pytest.mark.parametrize('test_input, expected, raises',
    [ #([5, 0.5], np.linspace(5, num=int(5/0.5 + 1)), None),
     ([5, 'a string'], None, ValueError),
     (['a string', 0.5], None, ValueError),
     ([5, 0], None, ValueError),
     ([0, 5], None, ValueError),
    ]
)
def test_generate_times(test_input, expected, raises):
    if raises:
        with pytest.raises(raises):
            assert generate_times(test_input) == expected
    else:
        assert generate_times(test_input) == expected

# Unit test for generate_compartments
@pytest.mark.parametrize('test_input, expected, raises',
    [ # ({'refcmpts': [[1, 1, 'Peripheral'], [1, 0.5, 'Main'], [1, 0.2, 'Sub']], 'model_type': 'sc'}, [Sub, Main, Peripheral], None),
    ({'refcmpts': [[15, 2, 'Peripheral'], [5, 1.5, 'Main'], [1, 0.2, 'Main']], 'model_type': 'ib'}, None, ValueError),
    ({'refcmpts': [[10, 10, 'Peripheral'], [1, 0.5, 'Sub'], [1, 0.2, 'Sub']], 'model_type': 'sc'}, None, ValueError)
])
def test_generate_compartments(test_input, expected, raises):
    from main.py import generate_compartments
    if raises:
        with pytest.raises(raises):
            assert generate_compartments(test_input) == expected
    else:
        assert generate_compartments(test_input) == expected

# Unit test for get_solution function
@pytest.mark.parametrize('test_input, expected, raises',
    [(['ingestion', 'subcmpt', 'maincmpt', 'peripherals', 2, 0.5, 12], None, AssertionError)
    ])
def test_get_solution(test_input, expected, raises):
    from solver import get_solution
    if raises:
        with pytest.raises(raises):
            assert get_solution(test_input) == expected

'''
@pytest.mark.parametrize('test_input, expected, raises',
    [([[1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']], None , None)
    ]
)
def test_form_rhs_ib(maincmpt, periph):

    form_rhs_ib(maincmpt, periph, calc_dose(2), 0.1)
    assert callable(form_rhs_ib)
'''
