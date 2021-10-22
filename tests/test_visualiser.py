print('Running tests on visualiser script')

def test_single_plot_data():
    from visualiser import single_plot_data

    json_file = './test_1.json'
    csv_file = './test_1.csv'

    assert len(single_plot_data(json_file, csv_file)) == 4
    assert type(single_plot_data(json_file, csv_file)[0]) == 'dict'
    assert type(single_plot_data(json_file, csv_file)[1]) == 'numpy.ndarray'

def test_collate_data():
    from visualiser import collate_data
    filesnames = [['test_1.json', 'test_1.csv'], ['test_2.json', 'test_2.csv']]

    assert len(collate_data(filesnames)) == len(filesnames)

def test_multiplot():
    from visualiser import multiplot

def test_makeplots():
    #Can we add a mock here to see what the function is calling Sam?
