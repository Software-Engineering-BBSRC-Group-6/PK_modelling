print("Running tests on user interface")


def test_user_input(monkeypatch):
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "ib")

    # go about using input() like you normally would:
    i = input("What kind of models do you want to build? (intravenous bolous (ib) / subcutaneous (sc))")
    assert i == "ib"
