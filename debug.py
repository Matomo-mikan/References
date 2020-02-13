#!/usr/bin/env python

import pdb # import pdb

ls = {"a": 10, "b": 20, "c": 30, "d": 20, "e": 50}

def key_from_value(i):

    pdb.set_trace() # set trace

    for key, val in ls.items():
        if val == i:
            return key

print(key_from_value(20))
