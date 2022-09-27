import Constants
import csv
import parse

#Testing the code of this project...
for fname, class_names, parser in zip(Constants.fnames, Constants.class_names, Constants.parsers):
    file_iter = parse.iter_file(fname, class_names, parser)
    print(fname)
    for _ in range(4):
        print(next(file_iter))
    print()
