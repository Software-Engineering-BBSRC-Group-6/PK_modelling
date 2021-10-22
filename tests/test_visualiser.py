print('Running tests on visualiser script')

# def test_single_plot_data():
#     import numpy 
#     from visualiser import single_plot_data

#     json_file = './test_json_ib.json'
#     csv_file = './test_csv.csv'

#     assert len(single_plot_data(json_file, csv_file)) == 4
#     assert type(single_plot_data(json_file, csv_file)[0]) == dict
#     assert type(single_plot_data(json_file, csv_file)[1]) == numpy.ndarray
 
# def test_collate_data():
#     from visualiser import collate_data
#     filesnames = [['./test_json_ib.json', './test_csv.csv'], ['./test_json_sc.json', './test_csv.csv']]

#     assert len(collate_data(filesnames)) == len(filesnames)

# @pytest.mark.parametrize('json_1, json_2, csv, expected_dimension',
#     [('./test_json_ib.json', './test_json_sc.json', './test_csv.csv',),
#      ('./test_json_ib.json', './test_json_ib.json', './test_csv.csv',),
#     ]
# )
# def test_multiplot():
    # from visualiser import multiplot
# For ib only
    # assert(axs.shape() == (1, compartments - 1))
    # func = multiplot(collate_data([['./test_json_ib.json', './test_csv.csv'], ['./test_json_sc.json', './test_csv.csv']]))
    # print(func.axs.shape())
 # For not ib only
    # assert(axs.shape() == (1, compartments))
    # print(axs.shape())
