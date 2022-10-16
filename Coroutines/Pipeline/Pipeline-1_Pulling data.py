import csv
import itertools

# Data parser
def parse_data(f_name):
    with open(f_name) as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)
        yield from csv.reader(f, dialect = dialect)


# Filtering data
def filter_data(rows, contains):
    for row in rows:
        if contains in row[0]:
            yield row

# Creating a delegator
def output(f_name, *filter_words):
    data = parse_data(f_name)
    for filter_word in filter_words:
        data = filter_data(data, filter_word)
    yield from data

results = output('cars.csv', 'Chevrolet', 'Carlo', 'Landau')
for row in itertools.islice(results, 5):
    print(row)
