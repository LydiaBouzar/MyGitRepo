# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:36:31 2024

@author: lbouzar
"""

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Test the function with a list of numbers
numbers = [10, 15, 20, 25, 30]
result = calculate_average(numbers)
print("The average is:", result)


missing_quote = 'This is a string with a missing closing quote.'
print(missing_quote)


my_list = [1, 2, 3, 4, 5]
print(my_list[10])


variable = 5 + variable
