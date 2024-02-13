# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:02:45 2024

@author: lbouzar
"""

def access_array_element(array, index):
    try:
        value = array[index]
        print(f"The value at index {index} is: {value}")
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the array.")

my_array = [1, 2, 3, 4, 5]
access_array_element(my_array, 2) 
access_array_element(my_array, 10)  
print("hello")
