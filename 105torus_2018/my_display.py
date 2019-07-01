#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## Maths
## File description:
## 105torus: display
##

import sys
import os

def my_print_usage():
    print("USAGE\n       ./105torus opt a0 a1 a2 a3 a4 n\n")
    print("DESCRIPTION")
    print("      opt             number of the option :")
    print("                             1 for the bisection method,")
    print("                             2 for Newton’s method,")
    print("                             3 for the secant method")
    print("      a0 ,a1 ,a2,a3 ,a4  coefficients of the equation")
    print("      n               precision (meaning the application of the polynomial to the solution") 
    print("                      should be smaller than 10-n)")
    return (0)

def my_check_arg():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            my_print_usage()
            sys.exit(0)
        else:
            print("USAGE\n       ./105torus opt a0 a1 a2 a3 a4 n\n")
            sys.exit(84)
    elif len(sys.argv) != 8:
        print("USAGE\n       ./105torus opt a0 a1 a2 a3 a4 n\n")
        sys.exit(84)
    if len(sys.argv) == 8:
        a = 1
        while a < 8:
            for d in sys.argv[a]:
                if ((d >= 'a' and d <= 'z') or (d >= 'A' and d <= 'Z')) and d != '-' and d != '+':
                    print("Int numbers only\n")
                    my_print_usage()
                    sys.exit(84)
            a += 1
        if len(sys.argv[1]) == 1:
            if sys.argv[1][0] != '1' and sys.argv[1][0] != '2' and sys.argv[1][0] != '3': 
                print("      opt             number of the option :")
                print("                             1 for the bisection method,")
                print("                             2 for Newton’s method,")
                print("                             3 for the secant method")
                sys.exit(84)
        else:
            my_print_usage()
            sys.exit(84)
