"""Python serial number generator."""

# from _typeshed import StrPath


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """Make a new generator, starting at start.
        Start defaults to 0 if no value is passed"""
        self.start = start
        self.original = start
    
    def generate(self):
        """Iterates start by one and returns previous start value"""
        self.start += 1
        return (self.start - 1)

    def reset(self):
        """Resets start value back to original passed in value"""
        self.start = self.original

    def __repr__(self):
        return f'SerialGenerator start={self.start - 1} next={self.start}'
        

