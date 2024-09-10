""" Module illustrating algorithm of Merge Sort"""
import rand

def merge_sort(arr):
    """Dividing the array"""
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    left_half = merge_sort(arr[:half])
    right_half = merge_sort(arr[half:])   
    return recombine(left_half, right_half)

def recombine(left_arr, right_arr):
    """Recombining the array"""
    left_index = 0
    right_index = 0
    merge_arr = []

    # Merging the two halves
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Append remaining elements of left_arr (if any)
    if left_index < len(left_arr):
        merge_arr.extend(left_arr[left_index:])
    # Append remaining elements of right_arr (if any)
    if right_index < len(right_arr):
        merge_arr.extend(right_arr[right_index:])

    return merge_arr

arr1 = rand.random_array([None] * 20)
arr2 = [1, 5, 4, 8, 2]
arr_out = merge_sort(arr2)

print(arr_out)
