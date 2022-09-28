import constants
import csv
import parse
import itertools
from datetime import datetime

#Testing the code of this project...
#for fname, class_names, parser in zip(constants.fnames, constants.class_names, constants.parsers):
#    file_iter = parse.iter_file(fname, class_names, parser)
#    print(fname)
#    for _ in range(4):
#        print(next(file_iter))
#    print()
    
#gen = parse.iter_combined(constants.fnames, constants.class_names, constants.parsers, compress_fields=constants.compress_fields)
#print(list(next(gen)))
#print(list(next(gen)))


#nt = parse.create_combo_namedtuple_class(constants.fnames, constants.compress_fields)
#print(nt._fields)

data_iter = parse.iter_combined_2(constants.fnames, constants.class_names,
                                  constants.parsers, constants.compress_fields)
for row in itertools.islice(data_iter, 5):
    print(row)
print('---------------------------------')
cutoff_date = datetime(2018,3,1)
filtered_iter = parse.filtered_iter_combined(constants.fnames, constants.class_names,
                                             constants.parsers, constants.compress_fields,
                                             key=lambda x: x.last_updated >= cutoff_date)
for row in filtered_iter:
    print(row)
