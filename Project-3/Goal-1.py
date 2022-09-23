# Creating a lazy iterator that will produce a namedtuple for each row of data.

from collections import namedtuple
from datetime import datetime
from functools import partial

f_name = 'nyc_parking_tickets_extract.csv'

with open(f_name) as f:
    column_headers = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')
    column_names = [header.replace(' ', '_').lower() for header in column_headers]
    Ticket = namedtuple('Ticket', column_names)

def read_data():
    with open(f_name) as f:
        next(f)
        yield from f

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default

def parse_date(value, *, default = None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default
    
def parse_string(value, *, default = None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default

column_parser = (parse_int,
                 parse_string,
                 lambda x: parse_string(x, default=''),
                 partial(parse_string, default=''),
                 parse_date,
                 parse_int,
                 partial(parse_string, default=''),
                 parse_string,
                 lambda x: parse_string(x, default='')
                 )

def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = [func(field) for func, field in zip(column_parser, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default

def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed
            
