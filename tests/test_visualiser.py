def test_single_plot_data():
    from visualiser import single_plot_data

    json_file = './test_json.json'
    csv_file = './test_csv.csv'

    assert len(single_plot_data(json_file, csv_file)) == 4
    assert type(single_plot_data(json_file, csv_file)[0]) == 'dict'
    assert type(single_plot_data(json_file, csv_file)[1]) == 'numpy.ndarray'