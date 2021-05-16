# Study on DNA Sequences of Anchoring based on Alignment Algorithm.

# Graduate_v_1.4
# C:\Users\jkkim\PycharmProjects\Graduate_2020_2\Start_11-22
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  GRP (Graduate Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 1.4
#  Rev. Date    : Nov. 23, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.7
# -----------------------------------------------------------------------------------------------------------
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    # key --> 값으로 입력될 문자
    # data --> 문자열의 종료를 알리는 flag
    # children --> 자식노드를 저장


class Nodes(object):
    def __init__(self):
        self.nodes = []

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

    def insertReference(self, string):

        if len(self.leafs) == 0:
            first = Nodes()
            first.append(Node(self.index, string))
            self.leafs.append(first)
            self.index += 1
            return
        else:
            for nodes in self.leafs:
                if string == nodes.nodes[0].data:
                    nodes.append(Node(self.index, string))
                    self.same = True

            if self.same is False:
                newNodes = Nodes()
                newNodes.append(Node(self.index, string))
                self.leafs.append(newNodes)

        self.index += 1
        # print(self.index)
        # print(self.leafs)

    def insert_q(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # curr_node --> 문자열
        curr_node.data = string

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
    Reference = ['bed', 'bad', 'bbb', 'bol', 'bom', 'bed', 'bol', 'bed', 'bbb']
    query = ['beo', 'bin']

    for k_mer_test_set in Reference:
        t.insertReference(k_mer_test_set)

    for k_mer_test_set2 in query:
        t.insert_q(k_mer_test_set2)

    # print('Rbed: ', t.search("bed"))
    # print('Qbin: ', t.search("bin"))

    print()
    print('Input:', Reference)
    print()
    print('Leafs:', '(', 'D',  ':', 'P', ')', end=" ")
    for nodes in t.leafs:
        print()
        for node in nodes.nodes:
            print('(', node.data, ':', node.key, ')', end=" "),
    print()
    print()

    print(t.leafs.nodes[3].node[0].data)

    # print('Leafs:', t.leafs[len(t.leafs) - 1].nodes[0].data)
