#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    message = dict()
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err.args[0]), file=sys.stderr)
        return (False)
