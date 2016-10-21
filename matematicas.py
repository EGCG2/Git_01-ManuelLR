#!/usr/bin/env python3

__author__ = "Manuel López Ruiz"

def suma(a, b):
    return a + b

def resta(a, b):
    return suma(a, -b)

a = 3
b = 2

print("a = " + str(a) + "; b = " + str(b))
print("resultado suma = " + str(suma(a, b)))
print("resultado resta = " + str(resta(a, b)))

