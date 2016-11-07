class Parameters(object):

    def __init__(self):
        self.vector = {}
        self.i = 0;

    def avanced(self):
        self.i = self.i + 1
        self.vector[self.i]

    def getvalue(self,a):
        return self.vector[a]

    def set_i(self,a):
        self.vector[a] = a

    def get_i(self,a):
        return self.vector
