from PIL import Image
from libs.perceptron.Addressable import *
from libs.perceptron.Sensor import *
from libs.perceptron.WeightForEachClassResolverBlock import WeightForEachClassResolverBlock as ResolverBlock
import random
import pickle

class Pyceptron(object):

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, **kwargs):
        '''kwargs: resolver_block, addressables_count'''
        self._addressables = []
        self._sensors = []
        self.resolver_block = kwargs.get("resolver_block", ResolverBlock())
        self.addressables_count = kwargs.get("addressables_count", 80)

    def resolve_path(self, path):
        image = Image.open(path)
        return self.resolve(image)

    def resolve(self, image):
        self.__initialize_sensors(image)
        if len(self._addressables) == 0:
            self.__initialize_addressables()
        return self.resolver_block.resolve_class()

    def learn(self, path, type):
        resolved_type = self.resolve_path(path)
        self.resolver_block.calibrate(type)

    def __initialize_sensors(self, image):
        px = image.load()
        for x in range(0, image.height):
            for y in range(0, image.width):
                index = image.width * x + y
                value = self.__get_pixel_value(px[y, x])
                if len(self._sensors) - 1 < index:
                    self._sensors.append(Sensor(value))
                else:
                    self._sensors[index].content = value

    def __initialize_addressables(self):
        self._addressables = [Addressable() for n in range(0, self.addressables_count)]
        for i in range(0, len(self._sensors)):
            index = random.randint(0, self.addressables_count - 1)
            self._addressables[index].add_sensor(i, self._sensors[i])
        self.resolver_block.addressables = self._addressables

    def __get_pixel_value(self, pixel):
        if pixel == self.BLACK or pixel == 0:
            return 1
        else:
            return 0

def save(obj, path):
    file = open(path, 'wb')
    pickle.dump(obj, file)

def load(path):
    file = open(path, 'rb')
    return pickle.load(file)