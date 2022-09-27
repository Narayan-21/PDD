import csv
from datetime import datetime
from collections import namedtuple

def csv_parse(fname, *, delimiter=',', quotechar='"', include_header=False):
    with open(fname) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        if not include_header:
            next(f)
        yield from reader

# Date Parser
def date_parse(value, * , fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)

#Returning only field names of a file using the csv_parse function created above.
def field_name(fname):
    reader = csv_parse(fname, include_header=True)
    return next(reader)

# Creating respective classes using namedtuple
def create_named_tuple_class(fname, class_name):
    fields = field_name(fname)
    return namedtuple(class_name, fields)

def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_parse(fname)
    for row in reader:
        parsed_data = (parse_fn(value) for value, parse_fn in zip(row, parser))
        yield nt_class(*parsed_data)
