#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary):
        keys = list(a_dictionary.keys())
        _best = [keys[0], a_dictionary[keys[0]]]

        for key in keys:
            value = a_dictionary[key]
            _best[0] = (value > _best[1]) and key
            _best[1] = (value > _best[1]) and value

        return (_best[0])

    return (None)
