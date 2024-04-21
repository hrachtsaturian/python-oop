"""Python serial number generator."""

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

    def __init__(self, start):
        self.accumulator = start - 1 
        self.start = start - 1

    def generate(self):
        """ function that generates number by adding one"""
        self.accumulator += 1 
        return self.accumulator
    
    def reset(self):
        self.accumulator = self.start

    
