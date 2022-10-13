# Creating an averager using generator.

def running_averager():
    total = 0
    count = 0
    running_avg = None
    while True:
        value = yield running_avg
        total += value
        count += 1
        running_avg = total/count

def running_averages(iterable):
    averager = running_averager()
    next(averager)
    for value in iterable:
        running_avg = averager.send(value)
        print(running_avg)

running_averages([1,2,3,4,5,6,7,8])
