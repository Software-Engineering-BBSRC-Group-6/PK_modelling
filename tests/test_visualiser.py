print('Running tests on visualiser script')

mockjsonib =  mock{
    "model_type": "ib",
    "compound": "paracetamol",
    "dose_type": "c",
    "dose": 0.5,
    "dose_mass": null,
    "time_dose": null,
    "num_dose": null,
    "len_assay": 72.0,
    "len_interval": 0.25,
    "clearance": 0.4,
    "compartments": [[1.0, 0.3, "Main"], [0.5, 0.15, "Heart"]],
    "vis": "y",
    "curr_datetime": "1634833362.6048021"}
mockcsv = StringIO("""\
0.00E+00,0.00E+00,0.00E+00,0.00E+00
2.50E-01,0.00E+00,2.33E-01,2.33E-01
5.00E-01,0.00E+00,4.19E-01,4.19E-01
7.50E-01,0.00E+00,5.50E-01,5.50E-01
1.00E+00,0.00E+00,6.32E-01,6.32E-01
1.25E+00,0.00E+00,6.77E-01,6.77E-01
1.50E+00,0.00E+00,6.95E-01,6.95E-01
1.75E+00,0.00E+00,6.94E-01,6.94E-01
2.00E+00,0.00E+00,6.81E-01,6.81E-01
2.25E+00,0.00E+00,6.59E-01,6.59E-01
2.50E+00,0.00E+00,6.32E-01,6.32E-01
2.75E+00,0.00E+00,6.02E-01,6.02E-01
3.00E+00,0.00E+00,5.71E-01,5.71E-01
3.25E+00,0.00E+00,5.38E-01,5.38E-01
3.50E+00,0.00E+00,5.06E-01,5.06E-01
3.75E+00,0.00E+00,4.75E-01,4.75E-01
4.00E+00,0.00E+00,4.45E-01,4.45E-01
4.25E+00,0.00E+00,4.16E-01,4.16E-01
4.50E+00,0.00E+00,3.88E-01,3.88E-01
4.75E+00,0.00E+00,3.62E-01,3.62E-01""")


def test_single_plot_data(mockjsonib,mockcsv):
    from visualiser import single_plot_data

    json_file = mockjsonib
    csv_file = mockcsv

    assert len(single_plot_data(json_file, csv_file)) == 4
    assert type(single_plot_data(json_file, csv_file)[0]) == 'dict'
    assert type(single_plot_data(json_file, csv_file)[1]) == 'numpy.ndarray'

def test_collate_data(mockjsonib,mockcsv):
    from visualiser import collate_data
    filesnames = [[mockjsonib, mockcsv], [mockjsonib, mockcsv]]

    assert len(collate_data(filesnames)) == len(filesnames)

def test_multiplot():
    from visualiser import multiplot

def test_makeplots():
    #Can we add a mock here to see what the function is calling Sam?
