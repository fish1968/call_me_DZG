import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, parentdir) 

import ADB_project

def future_care(func):
    def wrapper(*args, **kwargs):
        print("This function needs future attention!")
        return func(*args, **kwargs)
    return wrapper
