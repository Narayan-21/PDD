import csv
from contextlib import contextmanager

# Parsing data
def parse_data(f_name):
    f = open(f_name)
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)
        yield from csv.reader(f, dialect = dialect)
    finally:
        f.close()

def coroutine(fn):
    def inner(*args, **kwargs):
        g= fn(*args, **kwargs)
        next(g)
        return g
    return inner

# Writing and saving the rows in the output file.
@coroutine
def save_csv(f_name):
    with open(f_name, 'w', newline='') as f:
        writer = csv.writer(f)
        while True:
            row = yield
            writer.writerow(row)

# With filter_pred being the function that we will apply to the data
# and target being the function where we will propagate the filtered data.
@coroutine
def filter_data(filter_pred, target):
    while True:
        row = yield
        if filter_pred(row):
            target.send(row)

@coroutine
def pipeline_coro(out_file, name_filters):
    save = save_csv(out_file)

    target = save
    for name_filter in name_filters:
        target = filter_data(lambda d, v=name_filter: v in d[0], target)

    while True:
        received = yield
        target.send(received)

@contextmanager
def pipeline(out_file, name_filters):
    p = pipeline_coro(out_file, name_filters)
    try:
        yield p
    finally:
        p.close()

with pipeline('out.csv', ('Chevrolet', 'Landau', 'Carlo')) as p:
    for row in parse_data('cars.csv'):
        p.send(row)

with open('out.csv') as f:
    for row in f:
        print(row)
