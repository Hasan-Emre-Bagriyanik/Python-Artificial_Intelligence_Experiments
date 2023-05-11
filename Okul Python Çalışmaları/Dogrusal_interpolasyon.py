# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:11:19 2023

@author: Hasan Emre
"""

def f(x):
    return x**3 - 5*x**2 + 9*x - 1

a, b = 0, 1
tol = 0.01
max_iter = 100
max_error = tol

# initial interval
fa, fb = f(a), f(b)
if fa * fb > 0:
    raise ValueError("Function does not change sign on the interval.")

# linear interpolation
xn = a * fb - b * fa / (fb - fa)
i = 1
while i <= max_iter:
    error = max(abs(xn - a), abs(b - xn))
    if error < max_error:
        break
    if fa * f(xn) < 0:
        b = xn
    else:
        a = xn
    fa, fb = f(a), f(b)
    xn = a * fb - b * fa / (fb - fa)
    i += 1


print("Approximate root:", xn)

