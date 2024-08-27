from myfile import add_numbers

def true_test():
    assert add_numbers(1,2) == 3

def false_test():
    assert add_numbers(1,1) == 11

print(true_test())
print(false_test())

