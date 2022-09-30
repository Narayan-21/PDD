# Creating a precision context manager
import decimal

class Precision:
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec
    def __enter__(self):
        decimal.getcontext().prec = self.prec
    def __exit__(self, exc_type, exc_val, tb):
        decimal.getcontext().prec = self.current_prec
        return False
