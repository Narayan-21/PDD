import constants
import csv
import parse

#Testing the code of this project...
#for fname, class_names, parser in zip(constants.fnames, constants.class_names, constants.parsers):
#    file_iter = parse.iter_file(fname, class_names, parser)
#    print(fname)
#    for _ in range(4):
#        print(next(file_iter))
#    print()
    
gen = parse.iter_combined(constants.fnames, constants.class_names, constants.parsers, compress_fields=constants.compress_fields)
print(list(next(gen)))
print(list(next(gen)))
