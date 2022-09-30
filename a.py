from contextlib import contextmanager

@contextmanager
def open_file(fname):
    print(f'opening {fname}')
    f= open(fname)
    try:
        yield f
    finally:
        print(f'closing {fname}')
        f.close()

fnames = 'file1.txt', 'file2.txt', 'file3.txt'

# Creating and entering the context managers
exits=[]
enters=[]
for file in fnames:
    ctx = open_file(file)
    enters.append(ctx.__enter__)
    exits.append(ctx.__exit__)

# Entering the context managers.
files = [enter() for enter in enters]

# Working with the files
while True:
    try:
        rows = [next(f).strip('\n') for f in files]
    except StopIteration:
        break
    else:
        row = ','.join(rows)
        print(row)
        
# Exiting the context managers.
for exit in exits[::-1]:
    exit(None, None, None)
