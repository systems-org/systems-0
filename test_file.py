from myfile.py import add_numbers

def true_test():
    assert add_numbers(1,2) == 3

def false_test():
    assert add_numbers(1,1) == 11

