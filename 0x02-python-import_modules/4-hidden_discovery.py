#!/usr/bin/python3
import hidden_4

def read_hidden():
    for prop in dir(hidden_4):
        if prop[:2] != "__":
            print(prop)

if __name__ == "__main__":
    read_hidden()
