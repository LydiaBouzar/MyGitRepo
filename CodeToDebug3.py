# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:05:02 2024

@author: lbouzar
"""

def calculate_total_price(products):
    total_price = 0
    
    for product in products:
        
        total_price += product['price']
    
    return total_price


products_list = [
    {'name': 'Product A', 'price': 10},
    {'name': 'Product B', 'price': 20},
    {'name': 'Product C', 'price': 15}
    {'name': 'Product D', 'price': 20}
]


total_price = calculate_total_price(products_list)


