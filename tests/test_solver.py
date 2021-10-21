print("Running some unit tests")


def test_class():
    print("Testing class initialisation")

    from solver import Compartment
    c = Compartment(1, 1)
    assert c.volume == 1
