print("Running tests on user interface")


def test_user_input_model_type(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "ib")
    i = input("What kind of models do you want to build? (intravenous bolous (ib) / subcutaneous (sc))")
    assert i == "ib"

def test_user_input_dose_type(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "c")
    i = input("How is the dose delivered? Constantly over time (c), Instantaneously (i) or Repeated instantaneous doses (r): ")
    assert i == "c"

def test_user_input_dose(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("What is the dose of " + "compound" + " that you want to test? (units in ng per hour): "))
    assert i == 0.1

def test_user_input_dose_mass(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("What is the mass of the dose of " + "compound" + " that you want to test? (units in ng): "))
    assert i == 0.1

def test_user_input_time_dose(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("What time period are the doses given over? (units in hours): "))
    assert i == 0.1

def test_user_input_num_dose(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("How many doses are given? - this program assumes that doses are evenly spaced throughout the time period: "))
    assert i == 0.1

def test_user_input_num_dose(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("What time period would you like to simluate the model? (units in hours): "))
    assert i == 0.1

def test_user_input_len_interval(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("What interval time would you like in the simulation? (units in hours): "))
    assert i == 0.1

def test_user_input_len_interval(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.1)
    i = float(input("What is the clearance rate? (units in ng/hour): "))
    assert i == 0.1