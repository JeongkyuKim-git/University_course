# Study on DNA Sequences of Anchoring based on Alignment Algorithm.

# Graduate_v_4.1
# C:\Users\jkkim\PycharmProjects\Graduate_2020_2\Start_11-22
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  GRP (Graduate Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 4.1
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
        if curr_node.data is not None:
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
            if curr.data is not None:
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
    k_mer_test = []  # k-mer splice_window
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
    result_r = w.k_mer(reference_file.read().strip(), int(k_mer_user))
    result_q = w.k_mer(query_file.read().strip(), int(k_mer_user))

    for i in result_r:
        k_mer_test.append(i)

    for j in result_q:
        k_mer_query.append(j)

    print(reference_file.read())

    print("\n=================================== Change to k-mer ====================================")
    print("reference k-mer:    ", k_mer_test)
    print("reference_sequence: ACCCCGGTTCA\n")
    print("query k-mer:        ", k_mer_query)
    print("query_sequence:     CCCAACGTTTA")

    # ACCGGGTATA
    t = Match_Strtree()
    for k_mer_test_set in k_mer_test:
        t.insert(k_mer_test_set)

    print("\n================================= Find the same string =================================")
    print('ACCCCGGTTC: ', t.search("ACCCCGGTTC"))
    print('CCCAACGTTG: ', t.search("CCCAACGTTG"))

    print("\n============================= Categories in the lower root =============================")
    print('root_Virtual')
    print('root_A', t.starts_with("A"))
    print('root_C', t.starts_with("C"))
    print('root_G', t.starts_with("G"))
    print('root_T', t.starts_with("T"))

    """
    print("\n==================================== string search =====================================")
    print('Start_Node_CC', t.starts_with("CC"))
    """

    reference_file.close()
    query_file.close()
    print("\n=============================================================================================")
    print('current time :', (time.time() - start))
    print("=============================================================================================")
