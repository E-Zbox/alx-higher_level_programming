#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

operators = [
        '+', '-', '*', '/'
        ]
operators_func = [
        add, sub, mul, div
        ]
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

if (argv[2] in operators):
    index = operators.index(argv[2])
    result = operators_func[index](int(argv[1]), int(argv[3]))

    print(f"{argv[1]} {operators[index]} {argv[3]} = {result}")
else:
    print("Unknown operators. Available operators: +, -, * and /")
    exit(1)
