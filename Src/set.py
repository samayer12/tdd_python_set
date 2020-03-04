class Set:

    def __init__(self, size=None):
        if size is None:
            self.data = []
        else:
            self.data = [None] * size

    def __findEmpty__(self):
        if self.data[-1] is None:
            return self.data.index(None)

    def getSize(self):
        return len(self.data)

    def getCapacity(self):
        return self.data.count(None)

    def add(self, element):
        if self.data.__eq__([]):
            self.data = [element]
        elif None in self.data:
            self.data[self.__findEmpty__()] = element
        elif element not in self.data:
            self.data.append(element)

    def remove(self, element):
        self.data.remove(element)
