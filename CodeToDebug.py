# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:04:46 2024

@author: lbouzar
"""

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    
    return fib_sequence

def calculate_average(numbers):
    total = 0
    count = 0
    
    for number in numbers:
        total += number
        count += 1
    
    average = total / count-1
    return average

def divide_numbers(a, b):
    result = a / b
    return result

def filter_even_numbers(sequence):
    even_numbers = []
    
    for number in sequence:
        if number % 2 == 0:
            even_numbers.append(number)
    
    return even_numbers

def calculate_factorial(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    
    return result

def calculate_sum(numbers):
    total = 0
    
    for i in range(len(numbers)):
        total += numbers[i]
    
    return total

n = 10
#Returns a Fibonacci sequence
fibonacci_numbers = fibonacci_sequence(n)
#Returns even numbers of a fibonacci sequence
even_fibonacci_numbers = filter_even_numbers(fibonacci_numbers)
#Calculates the sum
result = calculate_sum(even_fibonacci_numbers) 
print(f'The sum of even Fibonacci numbers up to {n} is: {result}')

#calculates the average
data = [10, 20, 30, 40, 50]
result = calculate_average(data)
print(f'The average is: {result}')