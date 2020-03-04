class Set:

    def __init__(self, size=None):
        if size is None:
            self.data = []
        else:
            self.data = [None] * size

    def getSize(self):
        return 10

    def add(self, element):
        if self.data.__eq__([]):
            self.data = [element]
        elif element not in self.data:
            self.data.append(element)
        else:
            pass
