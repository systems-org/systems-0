from hw2_debugging import merge_sort
def true_test1():
  arr=[1,5,4,8,2]
  assert merge_sort(arr)==[1,2,4,5,8]
def true_test2():
  arr=[2] 
  assert merge_sort(arr)==[2]
def true_test3():
  arr=[1,4,5,6]
  assert merge_sort(arr)==[1,4,5,6]
