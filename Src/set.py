class Set:

    def __init__(self, size=None):
        if size is None:
            self.data = []
        else:
            self.data = [None] * size

    def getSize(self):
        return len(self.data)

    def add(self, element):
        if self.data.__eq__([]):
            self.data = [element]
        elif element not in self.data:
            if self.data[-1] is None:
                replacement_index = self.data.index(None)
                self.data[replacement_index] = element
            else:
                self.data.append(element)
        else:
            pass

    def getCapacity(self):
        return self.data.count(None)
