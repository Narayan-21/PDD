# Creating an iterator which also works as an Context manager.

class DataIterator:
    def __init__(self, fname):
        self._fname = fname
        self._f = None

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self._f)
        return row.strip('\n').split(',')

    def __enter__(self):
        self._f = open(self._fname)
        return self

    def __exit__(self, exc_type, exc_val, cb):
        if not self._f.closed:
            self._f.close()
        return False

with DataIterator('nyc_parking_tickets_extract.csv') as data:
    for row in data:
        print(row)
