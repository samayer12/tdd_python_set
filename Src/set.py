class Set:
    myData = None
    def create(self, size=None):
        if size is None:
            myData = []
        else:
            myData = [None] * size
        return myData

    def getSize(self):
        return 10