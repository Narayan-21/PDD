import itertools

with open('cars_2014.csv') as f:
    next(f)
    make_groups = itertools.groupby(f, key=lambda x:x.split(',')[0])
    make_counts = ((key, sum(1 for model in models)) for key, models in make_groups)
    print(list(make_counts))
