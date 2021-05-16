# Study on DNA Sequences of Anchoring based on Alignment Algorithm.

# Graduate_v_1.2
# C:\Users\jkkim\PycharmProjects\Graduate_2020_2\Start_11-22
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  GRP (Graduate Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 1.2
#  Rev. Date    : Nov. 22, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.7
# -----------------------------------------------------------------------------------------------------------
import time


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    # key --> 값으로 입력될 문자
    # data --> 문자열의 종료를 알리는 flag
    # children --> 자식노드를 저장


class Match_Strtree(object):
    """
    Insert, Search
    """

    def __init__(self):
        self.head = Node(None)

    """ #1__ insert """
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # curr_node --> 문자열
        curr_node.data = string

    """ #2__ Search """
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # curr_node에 데이터 유/무  (유)문자열 존재
        if (curr_node.data != None):
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

def window_size(local__file_size, local__k_size):
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
    k_mer_test = []  # k-mer splice_window
    k_mer_query = []  # k-mer splice_window
    """list_value"""

    local__string: str = ''
    local__number: int = 0
    """_value"""

    print("No_ k-mer <= 2, Using_ k-mer >= 3")
    k_mer_size = input('Please input the k-mer size:\n')  # input k-mer 'k'
    start = time.time()

    window_size(local__string, local__number)
    result_r = window_size(reference_file.read(), int(k_mer_size))
    result_q = window_size(query_file.read(), int(k_mer_size))

    for i in result_r:
        k_mer_test.append(i)

    for j in result_q:
        k_mer_query.append(j)

    print("\n---- k-mer size ----")
    print(k_mer_test, ": reference sequence")
    print(k_mer_query, ": query sequence\n")

    print("---- String tree find ----")
    # ACCGGGTATA
    t = Match_Strtree()
    for k_mer_test_set in k_mer_test:
        t.insert(k_mer_test_set)

    print('ACCCCGGTTC: ', t.search("ACCCCGGTTC"))
    print('CCCAACGTTG: ', t.search("CCCAACGTTG"))

    print("\n---- string root search ----")
    print('root_A', t.starts_with("A"))
    print('root_C', t.starts_with("C"))
    print('root_G', t.starts_with("G"))
    print('root_T', t.starts_with("T"))

    print("\n---- string search ----")
    print('Start_Node_CC', t.starts_with("CC"))

    reference_file.close()
    query_file.close()
    print('\n---- time ----')
    print('current time :', (time.time() - start))
