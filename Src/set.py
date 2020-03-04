class Set:

    def __init__(self, size=None):
        if size is None:
            self.data = []
        else:
            self.data = [None] * size

    def getSize(self):
        return 10
