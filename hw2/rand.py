""" Module to generate random number to fill the array"""
import subprocess

def random_array(arr):
    """ Generating the random array"""
    shuffled_num = None
    for i, inner_arr in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check= False)
        inner_arr[i] = int(shuffled_num.stdout)
    return arr
