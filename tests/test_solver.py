from pk_model.definitions import Compartment, form_rhs_ib
from pk_model.solver import generate_times, generate_compartments, get_solution
import numpy as np
import pytest

print("Running some unit tests")

#unit test for generate_time
@pytest.mark.parametrize('test_input, expected, raises',
    [([5, 0.5], np.linspace(0, 5, num=int(5/0.5 + 1)), None),
     ([5, 'a string'], None, TypeError),
     (['a string', 0.5], None, TypeError),
     ([5, 0], None, ValueError),
     ([0, 5], None, ValueError),
    ]
)
def test_generate_times(test_input, expected, raises):
    if raises:
        pytest.raises(raises, generate_times, *test_input)
    else:
        print(generate_times(*test_input))
        assert np.array_equal(generate_times(*test_input), expected)

# Unit test for generate_compartments
"""
@pytest.mark.parametrize('test_input, raises',
    [({'compartments': [[1, 1, 'Peripheral'], [1, 0.5, 'Main'], [1, 0.2, 'Sub']], 'model_type': 'sc'}, None),
    ({'compartments': [[15, 2, 'Peripheral'], [5, 1.5, 'Main'], [1, 0.2, 'Main']], 'model_type': 'ib'}, None),
    ({'compartments': [[10, 10, 'Peripheral'], [1, 0.5, 'Sub'], [1, 0.2, 'Sub']], 'model_type': 'sc'}, None),
])
def test_generate_compartments(test_input, raises):
    pytest.raises(raises, generate_compartments, test_input)
"""

# Unit test for get_solution function
"""
@pytest.mark.parametrize('test_input, expected, raises',
    [(['ingestion', 'subcmpt', 'maincmpt', 'peripherals', 2, 0.5, 12], None, AssertionError)
    ])
def test_get_solution(test_input, expected, raises):
    if raises:
        with pytest.raises(raises):
            assert get_solution(test_input) == expected
"""
"""
@pytest.mark.parametrize('test_input',
    [([[1, 0.5, 'Main'], [[1, 1, 'Peripheral'], [0.5, 0.5, 'Peripheral']]]),
    ]
)
def test_form_rhs_ib(test_input, expected, raises):

    form_rhs_ib(test_input[0], test_input[1], calc_dose(2), 0.1)
    assert callable(form_rhs_ib)
"""
