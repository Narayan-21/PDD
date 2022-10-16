# Creating an averager coroutine that outsource the calculated average in
# a file named sample.csv

class WriteAverage(Exception):
    pass

def averager(out_file):
    total = 0
    count = 0
    average = None
    with open(out_file, 'w') as f:
        f.write('count, average\n')
        while True:
            try:
                received = yield average
                total += received
                count += 1
                average = total/count
            except WriteAverage:
                if average is not None:
                    print('Saving average to file:', average)
                    f.write(f'{count}, {average}\n')

avg = averager('sample.csv')
next(avg)
# Sending some random values to the 'yield' in the coroutine
avg.send(10)
avg.send(11)
avg.send(12)
avg.throw(WriteAverage)
avg.send(20)
avg.throw(WriteAverage)
avg.close()

with open('sample.csv') as f:
    for row in f:
        print(row.strip())
        
# Using the delegator
def delegator():
   yield from averager('sample.csv')

d=delegator()
next(d)
d.send(3)
d.send(5)
d.throw(WriteAverage)
d.close()
# Reading the created sample.csv file back

with open('sample.csv') as f:
    for row in f:
        print(row.strip())
