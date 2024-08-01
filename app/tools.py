from os import path

def href(*args):
    return path.join(path.dirname(path.abspath(__file__)), *args)