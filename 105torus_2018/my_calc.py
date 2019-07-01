#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## Maths
## File description:
## 105torus
##

import math as m
import sys
import os

def my_bisection(CF, n):
    p1 = 0.0
    p2 = 1.0
    x1 = float
    x2 = float
    x = float

    for i in range(1, 300):
        x = (p1 + p2) / 2
        if i <= n:
            print("x = {0:.{1:d}f}".format(x, i))
        else:
            print("x = {0:.{1:d}f}".format(x, n))
        x1 = (CF.a4 * pow(x, 4)) + (CF.a3 * pow(x, 3)) + (CF.a2 * pow(x, 2)) + (CF.a1 * x) + CF.a0
        x2 = (CF.a4 * pow(p1, 4)) + (CF.a3 * pow(p1, 3)) + (CF.a2 * pow(p1, 2)) + (CF.a1 * p1) + CF.a0
        if x2 * x1 < 0:
            p2 = x
        else:
            p1 = x
        if round(p1 * pow(10, n)) == round(p2 * pow(10, n)):
            exit (0)
def my_newton(CF, n):
    p1 = 0.0
    p2 = 1.0
    x1 = float
    x2 = float
    x = float

    for i in range(1, 300):
        x = (p1 + p2) / 2
        if i <= n:
            print("x = {0:.{1:d}f}".format(x, i))
        else:
            print("x = {0:.{1:d}f}".format(x, n))
        x1 = (CF.a4 * pow(x, 4)) + (CF.a3 * pow(x, 3)) + (CF.a2 * pow(x, 2)) + (CF.a1 * x) + CF.a0
        x2 = (CF.a4 * pow(p1, 4)) + (CF.a3 * pow(p1, 3)) + (CF.a2 * pow(p1, 2)) + (CF.a1 * p1) + CF.a0
        if x2 * x1 < 0:
            p2 = x
        else:
            p1 = x
        if round(p1 * pow(10, n)) == round(p2 * pow(10, n)):
            exit (0)

def my_secant(CF, n):
    print("Secant:")
    print("a0 = {0:d}".format(CF.a0))
    print("a1 = {0:d}".format(CF.a1))
    print("a2 = {0:d}".format(CF.a2))
    print("a3 = {0:d}".format(CF.a3))
    print("a4 = {0:d}".format(CF.a4))
    print("n = {0:d}".format(n))
