import csv
from contextlib import contextmanager
from collections import namedtuple
from itertools import islice




@contextmanager
def parsed_data(f_name):
    f=open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda s: s.lower(), next(reader))
        nt = namedtuple('Data', headers)
        yield (nt(*row) for row in reader)
    finally:
        f.close()

with parsed_data('personal_info.csv') as data:
    for row in islice(data, 5):
        print(row)
with parsed_data('cars.csv') as data:
    for row in islice(data, 5):
        print(row)
