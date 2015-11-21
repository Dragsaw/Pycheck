class PageNotFoundException(Exception):
    """ Is raised when page was not found. """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


