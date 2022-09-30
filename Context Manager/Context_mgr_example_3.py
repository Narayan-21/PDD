# Creating a StdOut file as a context manager

import sys
class OutFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout
    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file
    def __exit__(self, typ, val, tb):
        sys.stdout = self._current_stdout
        self._file.close()
        return False

with OutFile('test.txt'):
    print('Another Context manager example')
