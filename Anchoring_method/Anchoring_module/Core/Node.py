class Node(object):

    def __init__(self, key, data=None, sequence='R'):
        self.key = key
        self.children = {}
        self.notVisited = True

    def __repr__(self):
        # return "[" + str(self.data) + ", " + str(self.key) + ", " + str(self.sequence) + ", " + str(
        #     self.notVisited) + "]"
        return self.key
