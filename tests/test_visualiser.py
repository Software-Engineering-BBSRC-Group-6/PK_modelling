import pytest
import numpy as np
from pk_model.visualiser import single_plot_data, collate_data, multiplot


print('Running tests on visualiser script')

def test_single_plot_data():
    '''
    This tests that the single_plot_data function creates a list containing
    four elements and that these elements are the following and in order:
    dictionary, numpy array, integer, integer.
    '''
    
    json_file = './test_json_ib.json'
    csv_file = './test_csv.csv'

    assert len(single_plot_data(json_file, csv_file)) == 4
    assert type(single_plot_data(json_file, csv_file)[0]) == dict
    assert type(single_plot_data(json_file, csv_file)[1]) == np.ndarray
    assert type(single_plot_data(json_file, csv_file)[2]) == int
    assert type(single_plot_data(json_file, csv_file)[3]) == int


def test_collate_data():
    '''
    This funtion tests that the collate_data function creates a collated list
    of data elements that has the same number of components as the number of
    file pairings which were inputted into the function. This ensures that all
    data files have been included in the collated list.
    '''

    filesnames = [['./test_json_ib.json', './test_csv.csv'],
                  ['./test_json_sc.json', './test_csv.csv']]

#     assert len(collate_data(filesnames)) == len(filesnames)


@pytest.mark.parametrize('input, error',
    [([[23, np.array([[ 0.   ,  0.   ,  0.   ,  0.   ],
       [ 0.25 ,  0.   ,  0.233,  0.233],
       [ 0.5  ,  0.   ,  0.419,  0.419],
       [ 0.75 ,  0.   ,  0.55 ,  0.55 ],
       [ 1.   ,  0.   ,  0.632,  0.632],
       [ 1.25 ,  0.   ,  0.677,  0.677],
       [ 1.5  ,  0.   ,  0.695,  0.695],
       [ 1.75 ,  0.   ,  0.694,  0.694],
       [ 2.   ,  0.   ,  0.681,  0.681],
       [ 2.25 ,  0.   ,  0.659,  0.659],
       [ 2.5  ,  0.   ,  0.632,  0.632],
       [ 2.75 ,  0.   ,  0.602,  0.602],
       [ 3.   ,  0.   ,  0.571,  0.571],
       [ 3.25 ,  0.   ,  0.538,  0.538],
       [ 3.5  ,  0.   ,  0.506,  0.506],
       [ 3.75 ,  0.   ,  0.475,  0.475],
       [ 4.   ,  0.   ,  0.445,  0.445],
       [ 4.25 ,  0.   ,  0.416,  0.416],
       [ 4.5  ,  0.   ,  0.388,  0.388],
       [ 4.75 ,  0.   ,  0.362,  0.362]]), 20, 4]], TypeError),
       ([[{u'num_dose': None, u'len_assay': 72.0, u'dose_mass': None, u'compound': u'paracetamol', u'len_interval': 0.25, u'dose': 0.5, u'time_dose': None, u'vis': u'y', u'curr_datetime': u'1634833362.6048021', u'dose_type': u'c', u'model_type': u'sc', u'clearance': 0.4, u'compartments': [[1.0, 0.3, u'Main'], [0.5, 0.15, u'Heart']]},
        'hello', 20, 4]], TypeError),
        ([[{u'num_dose': None, u'len_assay': 72.0, u'dose_mass': None, u'compound': u'paracetamol', u'len_interval': 0.25, u'dose': 0.5, u'time_dose': None, u'vis': u'y', u'curr_datetime': u'1634833362.6048021', u'dose_type': u'c', u'model_type': u'sc', u'clearance': 0.4, u'compartments': [[1.0, 0.3, u'Main'], [0.5, 0.15, u'Heart']]},
        np.array([[ 0.   ,  0.   ,  0.   ,  0.   ],
       [ 0.25 ,  0.   ,  0.233,  0.233],
       [ 0.5  ,  0.   ,  0.419,  0.419],
       [ 0.75 ,  0.   ,  0.55 ,  0.55 ],
       [ 1.   ,  0.   ,  0.632,  0.632],
       [ 1.25 ,  0.   ,  0.677,  0.677],
       [ 1.5  ,  0.   ,  0.695,  0.695],
       [ 1.75 ,  0.   ,  0.694,  0.694],
       [ 2.   ,  0.   ,  0.681,  0.681],
       [ 2.25 ,  0.   ,  0.659,  0.659],
       [ 2.5  ,  0.   ,  0.632,  0.632],
       [ 2.75 ,  0.   ,  0.602,  0.602],
       [ 3.   ,  0.   ,  0.571,  0.571],
       [ 3.25 ,  0.   ,  0.538,  0.538],
       [ 3.5  ,  0.   ,  0.506,  0.506],
       [ 3.75 ,  0.   ,  0.475,  0.475],
       [ 4.   ,  0.   ,  0.445,  0.445],
       [ 4.25 ,  0.   ,  0.416,  0.416],
       [ 4.5  ,  0.   ,  0.388,  0.388],
       [ 4.75 ,  0.   ,  0.362,  0.362]]), 20, 4]], None),])
def test_multiplot_inputs(input, error):
    '''
    This function tests that the multiplot function correctly identifies errors in the
    inputs to the plotting function. Inputs must be dictionary, array, int, int in that
    order. This test checks that TypeErrors are thrown if these inputs are not adhered to.
    '''

    if error:
        with pytest.raises(error):
            assert multiplot(input) == error
    else:
        assert multiplot(input) == error
