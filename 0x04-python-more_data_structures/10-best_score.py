#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxx = max(a_dictionary.values())
        for name, i in a_dictionary.items():
            if i == maxx:
                return name
