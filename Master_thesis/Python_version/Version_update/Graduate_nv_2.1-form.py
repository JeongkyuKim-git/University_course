# Study on DNA Sequences of Anchoring based on Alignment Algorithm.

# Graduate_v_2.1
# C:\Users\jkkim\PycharmProjects\Graduate_2020_2\Start_11-22
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  GRP (Graduate Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 2.1
#  Rev. Date    : Nov. 22, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.7
# -----------------------------------------------------------------------------------------------------------
import time


class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # key --> 값으로 입력될 문자
        self.data = data  # data --> 문자열의 종료를 알리는 flag
        self.children = {}  # children --> 자식노드를 저장


class Match_str_tree(object):
    """
    Insert, Search
    """
    index = 0
    index_2 = 0

    def __init__(self):  # __init__ (start)
        self.head = Node(None)  # head --> this point
        self.list_r_call = []

    """ #1__ insert """

    def insert(self, string):  # created reference tree
        curr_node = self.head  # curr --> current node (현재 노드)

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)  # Character (single char) --> node

            curr_node = curr_node.children[char]

        curr_node.data = string  # curr_node.data --> leaf node (문자열)

        self.list_r_call.append([curr_node.data, self.index])
        self.index = self.index + 1

        """
        count = 0
        count = count + 1

        for i in range(count):
            line = []
            if count > len(self.list_r_call):
                break;
            for j in range
                line.append(0)
            a.append(line)
        """

        # count > len(self.list_r_call)
        """
        for i in range(self.list_r_call):
            for j in range(self.list_r_call):
                if self.list_r_call[i][0] == self.list_r_call[j][0]:
                    self.list_r_call[i].append(self.list_r_call[j])
                else:
                    self.list_r_call.append((curr_node.data, self.index))
                    self.index = self.index + 1
        """
    """ #2__ Search """

    def search(self, string):  # check query / check reference
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data is not None:  # curr_node에 데이터 유/무  (유)문자열 존재
            return True

    """ String exact match """

    def starts_with(self, prefix):  # String (find_character)
        curr_node = self.head
        result = []
        substring = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                substring = curr_node
            else:
                return None

        queue = list(substring.children.values())  # look for nodes with non-null data fields.

        while queue:
            curr = queue.pop(0)
            if curr.data is not None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result


class window_size(object):  # k-mer (k - size)
    """
    window_size spliced
    """

    def k_mer(self, local__file_size, local__k_size):
        for i in range(0, len(local__file_size) - (local__k_size - 1)):
            yield local__file_size[i:i + local__k_size]

    """k-mer size function"""


if __name__ == "__main__":  # __main__

    local__string: str = ''
    local__number: int = 0
    """_value"""

    reference_file = open('../sample.txt', 'r')  # reference file open
    """rf_file_value"""

    query_file = open('sample2.txt', 'r')  # query file open
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

    print("\n=================================== Changing to k-mer ====================================")
    print("reference k-mer:    ", k_mer_reference)
    print("reference_sequence:  ACCCCGGTTCA\n")
    print("query k-mer:        ", k_mer_query)
    print("query_sequence:      CCCAACGTTTA")

    # ACCGGGTATA
    t = Match_str_tree()
    for k_mer_test_set in k_mer_reference:
        t.insert(k_mer_test_set)

    print("\n================================= Finding of the same string =================================")
    """
    for k_mer_test_set in k_mer_query:
        if t.search(k_mer_test_set):
            t.insert(k_mer_test_set)
            print(k_mer_test_set)
    """
    goto_test = []
    print(t.list_r_call)
    goto_test = t.list_r_call

    for total in range(len(goto_test)):
        print(goto_test[total][0])

    print('TTA: ', t.search("TTA"))

    print("\n============================= Showing the graph =============================")
    print('root_Virtual')
    print('root_A', t.starts_with("A"))
    print('root_C', t.starts_with("C"))
    print('root_G', t.starts_with("G"))
    print('root_T', t.starts_with("T"))

    """
    print("\n==================================== Searching for string matches =====================================")
    print('Start_Node_CC', t.starts_with("CC"))
    """

    reference_file.close()
    query_file.close()
    print("\n=============================================================================================")
    print('current time :', (time.time() - start))
    print("=============================================================================================")
