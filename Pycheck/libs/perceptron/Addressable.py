import random

class Addressable(object):

    def __init__(self, **kwargs):
        self.sensors = dict()

    def add_sensor(self, index, sensor):
        self.sensors[index] = sensor

    @property
    def sum (self):
        result = 0
        for k in self.sensors:
            result += self.sensors[k].value
        return result

    def get_output(self, threshold):
        sum = self.sum
        if sum > threshold:
            return 1
        else:
            return 0