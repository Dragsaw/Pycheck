import random

class Sensor(object):

    def __init__(self, value, **kwargs):
        self.content = value
        self.multiplier = (-1) ** random.randint(1,2)

    @property
    def value (self):
        return self.content * self.multiplier