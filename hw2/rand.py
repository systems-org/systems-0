""" Module to generate random number to fill the array"""
import subprocess

def random_array(arr):
    """ Generating the random array"""
    shuffled_num = None
    for inner_arr in arr:
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        inner_arr[0] = int(shuffled_num.stdout.decode().strip())  
    return arr