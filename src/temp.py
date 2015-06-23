#! usr/bin/env python

"""This is a python module that converts F to K
"""

def f_to_k(temp):
    converted = (temp - 32) * 5.0/9.0 + 273.15
    return converted

def k_to_f(temp):
    converted = (temp-273.15)*9.0/5.0

print f_to_k(32)
