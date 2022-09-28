import csv
from datetime import datetime
from collections import namedtuple
import itertools

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

def create_combo_namedtuple_class(fnames, compress_fields):
    compress_fields = itertools.chain.from_iterable(compress_fields)
    field_names = itertools.chain.from_iterable(field_name(fname) for fname in fnames)
    compressed_field = itertools.compress(field_names, compress_fields)
    return namedtuple('Data', compressed_field)

def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_parse(fname)
    for row in reader:
        parsed_data = (parse_fn(value) for value, parse_fn in zip(row, parser))
        yield nt_class(*parsed_data)

def iter_combined(fnames, class_names, parsers, compress_fields):
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuple = zip(*(iter_file(fname, class_name, parser)
         for fname, class_name, parser in zip(fnames, class_names, parsers)))
    merged_iter = (itertools.chain.from_iterable(zipped_tuple)
                   for zipped_tuple in zipped_tuple)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield tuple(compressed_row)

def iter_combined_2(fnames, class_names, parsers, compress_fields):
    combo_nt = create_combo_namedtuple_class(fnames, compress_fields)
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuple = zip(*(iter_file(fname, class_name, parser)
         for fname, class_name, parser in zip(fnames, class_names, parsers)))
    merged_iter = (itertools.chain.from_iterable(zipped_tuple)
                   for zipped_tuple in zipped_tuple)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield combo_nt(*compressed_row)

def filtered_iter_combined(fnames, class_names, parsers, compress_fields, * ,key=None):
    iter_combo = iter_combined_2(fnames, class_names, parsers, compress_fields)
    yield from filter(key, iter_combo)
