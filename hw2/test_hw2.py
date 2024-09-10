from hw2_debugging import merge_sort

def test_true1():
    arr = [1, 5, 4, 8, 2]
    sorted_arr = merge_sort(arr)
    print(f"Test 1 - Output: {sorted_arr}")
    assert sorted_arr == [1, 2, 4, 5, 8]

def test_true2():
    arr = [2]
    sorted_arr = merge_sort(arr)
    print(f"Test 2 - Output: {sorted_arr}")
    assert sorted_arr == [2]

def test_true3():
    arr = [1, 4, 5, 6]
    sorted_arr = merge_sort(arr)
    print(f"Test 3 - Output: {sorted_arr}")
    assert sorted_arr == [1, 4, 5, 6]
