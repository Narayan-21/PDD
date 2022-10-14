from inspect import getgeneratorstate
import csv
import itertools

class TransactionAborted(Exception):
    pass

def save_to_db():
    print('Starting new transaction')
    id_abort = False
    try:
        while True:
            data = yield
            print('Sending data to database:', eval(data))
    except Exception as ex:
        id_abort = True
        raise TransactionAborted(str(ex))
    finally:
        if id_abort:
            print('Rollback transaction')
        else:
            print('Commit transaction')
trans = save_to_db()
next(trans)
trans.send('1+2')
trans.close()
