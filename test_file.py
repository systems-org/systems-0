# test_file.py

from myfile import add_numbers

def test_true():
    assert add_numbers(1, 2) == 3

def test_false():
    assert add_numbers(1, 1) == 2 # This should fail
