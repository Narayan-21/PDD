import csv
from itertools import islice
from collections import namedtuple

f_names = 'cars.csv', 'personal_info.csv'

def get_dilect(f_name):
    with open(f_name) as f:
        return csv.Sniffer().sniff(f.read(1000))

class FileParser:
    def __init__(self, f_name):
        self.f_name = f_name
    def __enter__(self):
        self._f = open(self.f_name, 'r')
        self._reader = csv.reader(self._f, get_dilect(self.f_name))
        headers = map(lambda s: s.lower(),next(self._reader))
        self._nt = namedtuple('Data', headers)
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._f.close()
        return False
    def __iter__(self):
        return self
    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._reader))

with FileParser(f_names[0]) as data:
    for row in islice(data, 10):
        print(row)
