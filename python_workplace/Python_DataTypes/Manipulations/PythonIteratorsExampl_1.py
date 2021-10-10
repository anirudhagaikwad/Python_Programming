""""
Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and __next__().
The __iter__() method returns the iterator object itself. If required, some initialization can be performed.
The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration
"""

""""
example that will give us next power of 2 in each iteration. 
Power exponent starts from zero up to a user set number
"""
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration