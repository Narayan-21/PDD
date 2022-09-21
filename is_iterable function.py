# Defining a function is_iterable that will return True if the object passed is
# iterable, False otherwise.

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
