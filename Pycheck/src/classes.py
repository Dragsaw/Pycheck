class Area(object):
    ''' Represents an area consisting only from white pixels. '''
    def __init__(self, start, end = -1):
        self.start = start
        self.end = end

    @property
    def length(self):
        return self.end - self.start

class PageNotFoundException(Exception):
    ''' Is raised when page was not found. '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Number(object):
    ''' Represents a number in images. '''
    def __init__(self, digits):
        self.digits = digits