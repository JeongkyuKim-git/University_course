# Study on DNA Sequences of Anchoring based on Alignment Algorithm.

# Graduate_v_3.1
# C:\Users\jkkim\PycharmProjects\Graduate_2020_2
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  GRP (Graduate Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 3.1
#  Rev. Date    : Nov. 23, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.7
# -----------------------------------------------------------------------------------------------------------
import time

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

    """ 위치 찾기 """
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # and look for nodes with non-null data fields.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop(0)
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result


class window_size(object):
    """
    window_size spliced
    """

    def k_mer(self, local__file_size, local__k_size):
        for i in range(0, len(local__file_size) - (local__k_size - 1)):
            yield local__file_size[i:i + local__k_size]
    """k-mer size function"""


if __name__ == "__main__":

    local__string: str = ''
    local__number: int = 0
    """_value"""

    reference_file = open('../sample.txt', 'r')  # file open reference
    """rf_file_value"""

    query_file = open('sample2.txt', 'r')  # file open reference
    """query_file_value"""

    Reference_list = []  # Reference_list = []
    k_mer_reference = []  # k-mer splice_window
    k_mer_query = []  # k-mer splice_window
    """list_value"""

    while (True):  # 무한 반복
        # 데이터 입력
        print("=============================================================================================")
        print("[* You don't input k-mer of this size <= 2 |* Please input more than k-mer of this size >= 3]")
        print("=============================================================================================")
        print()
        k_mer_user = input('Please input the k-mer size:\n')  # input k-mer 'k'

        # 예외 처리: 입력값이 정수가 아닌 경우 다시 입력
        if 'a' <= k_mer_user <= 'z':
            print(k_mer_user, "는 정수가 아닙니다. 다시 입력하시기 바랍니다.")
            continue

        elif 'A' <= k_mer_user <= 'Z':
            print(k_mer_user, "는 정수가 아닙니다. 다시 입력하시기 바랍니다.")
            continue

        elif 'ㄱ' <= k_mer_user <= 'ㅎ':
            print(k_mer_user, "는 정수가 아닙니다. 다시 입력하시기 바랍니다.")
            continue

        elif ' ' == k_mer_user:
            print(k_mer_user, "는 정수가 아닙니다. 다시 입력하시기 바랍니다.")
            continue

        # 예외 처리: 입력값이 정수가 아닌 경우 다시 입력
        elif int(k_mer_user) <= 2:
            print("2이하를 입력했습니다.")
            continue

        break  # 반복 중지

    start = time.time()

    w = window_size()
    result_r = w.k_mer(reference_file.read(), int(k_mer_user))
    result_q = w.k_mer(query_file.read(), int(k_mer_user))

    for i in result_r:
        k_mer_reference.append(i)

    for j in result_q:
        k_mer_query.append(j)

    print(reference_file.read())

    print("\n=================================== Change to k-mer ====================================")
    print("reference k-mer:    ", k_mer_reference)
    print("reference_sequence: ACCCCGGTTCA\n")
    print("query k-mer:        ", k_mer_query)
    print("query_sequence:     CCCAACGTTTA\n")

    print("\n================================= Find the same string =================================")
    t = Match_Strtree()
    for k_mer_test_set in k_mer_reference:
        t.insert(k_mer_test_set, 'R')

    for k_mer_test_set in k_mer_query:
        t.insert(k_mer_test_set, 'Q')

    print('CCC: ', t.search("CCC"))
    print('TTA: ', t.search("TTA"))

    print("\n============================= Categories in the lower root =============================")
    print('root_Virtual')
    print('root_A', t.starts_with("A"))
    print('root_C', t.starts_with("C"))
    print('root_G', t.starts_with("G"))
    print('root_T', t.starts_with("T"))

    print("\n============================= look-up table of Leaf node =============================")
    print(t.leafs)
    print(t.leafs[0])
    """
    print("\n==================================== string search =====================================")
    print('Start_Node_CC', t.starts_with("CC"))
    """

    reference_file.close()
    query_file.close()
    print("\n=============================================================================================")
    print('current time :', (time.time() - start))
    print("=============================================================================================")
