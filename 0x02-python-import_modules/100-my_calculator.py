#!/usr/bin/python3
import sys
from calculator_1 import div, add, sub, mul

ac = len(sys.argv)

if __name__ == "__main__":
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if op != "-" and op != "+" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
