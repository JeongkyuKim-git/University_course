class Node(object):
    def __init__(self, key, data=None, sequence='R'):
        self.key = key
        self.data = data
        self.children = {}
        self.sequence = sequence

    def __repr__(self):
        return "(" + self.data + ", " + str(self.key) + ", " + self.sequence + ")"

    # key --> 값으로 입력될 문자
    # data --> 문자열의 종료를 알리는 flag
    # children --> 자식노드를 저장


class Nodes(object):
    def __init__(self):
        self.nodes = []
        self.output = ''

    def toString(self):
        first = True
        self.output = '['
        for node in self.nodes:
            if first:
                self.output += str(node)
                first = False
            else:
                self.output += ', ' + str(node)

        self.output += ']'
        return self.output

    def __repr__(self):
        # return self.nodes
        return self.toString()

    def append(self, node):
        self.nodes.append(node)


class Match_Strtree(object):
    """
    Insert, Search
    """

    index = 0

    def __init__(self):
        self.head = Node(None)
        self.list_r_call = []
        self.leafs = []
        self.same = False

    """
    #1__ insert
    """
    def insert_r(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # curr_node --> 문자열
        curr_node.data = string

        self.list_r_call.append((curr_node.data, self.index))
        self.index = self.index + 1

        # print(self.list_r_call)

    def insert(self, string, sequence):

        if sequence == 'Q':
            for nodes in self.leafs:
                if string == nodes.nodes[0].data:
                    print(string, ': True')
                    self.same = True
                    break
            if self.same is False:
                print(string, ': False')
                return

        self.same = False

        if len(self.leafs) == 0:
            first = Nodes()
            first.append(Node(self.index, string, sequence))
            self.leafs.append(first)
            self.index += 1
            return
        else:
            for nodes in self.leafs:
                if string == nodes.nodes[0].data:
                    nodes.append(Node(self.index, string, sequence))
                    self.same = True

            if self.same is False:
                newNodes = Nodes()
                newNodes.append(Node(self.index, string, sequence))
                self.leafs.append(newNodes)

        self.same = False
        self.index += 1

    """
    #2__ Search
    """
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # curr_node에 데이터 유/무  (유)문자열 존재
        if curr_node.data != None:
            return True


if __name__ == "__main__":
    t = Match_Strtree()
    Reference = ['bed', 'bad', 'bbb', 'bol', 'bom', 'bed', 'bol', 'bed', 'bbb', 'bbb']
    Query = ['bin', 'bat', 'bad']

    print('Reference', Reference)
    print('Query', Query)
    print()

    for k_mer_test_set in Reference:
        t.insert(k_mer_test_set, 'R')

    t.index = 0
    for k_mer_test_set in Query:
        t.insert(k_mer_test_set, 'Q')

    print()
    print(t.leafs)
    print(type(t.leafs[1]))
