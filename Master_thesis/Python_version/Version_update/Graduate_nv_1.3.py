# Study on DNA Sequences of Anchoring based on Alignment Algorithm.

# Graduate_v_1.3
# C:\Users\jkkim\PycharmProjects\Graduate_2020_2\Start_11-22
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  GRP (Graduate Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 1.3
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


class Match_Strtree(object):
    """
    Insert, Search
    """
    index = 0

    def __init__(self):
        self.head = Node(None)
        self.list_r_call =[]

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

        """lookup table"""
        self.list_r_call.append((curr_node.data, 'R', self.index))
        self.index = self.index + 1

#       list_r_call.append((curr_node.data, i))
#        print(list_r_call)

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
        if (curr_node.data != None):
            return True


t = Match_Strtree()
Reference = ['bed', 'bad', 'bbb', 'bol', 'bombay', 'bed']
query = ['beo', 'bin', 'bed', 'bed']

#-------------------------------------------
common_list = []

for k_mer_test_set in Reference:
    t.insert_r(k_mer_test_set)

print(query)

print(Reference.index('bol'), "---- Check_query index")

for item in query:
    if t.search(str(item)) == True:
        print(query.index(str(item)))
        target = str(item)
        idx_q = query.index(str(target))
        common_list.append((str(item), 'Q', idx_q))

print(common_list) #common query_list

print('Rbed: ', t.search('bed'))
print('Qbin: ', t.search('bin'))
print('leaf_table:',t.list_r_call)
#-------------------------------------------
"""


for k_mer_test_set in Reference:
    t.insert_r(k_mer_test_set)

for k_mer_test_set2 in query:

    if (query[k_mer_test_set2] == True):
        k_mer_test_set2 + 1
        
    if (query == t.search())
        print(query)
    #else: t.insert_q(k_mer_test_set2)

print('Rbed: ', t.search("bed"))
print('Qbin: ', t.search("bin"))
print('leaf_table:',t.list_r_call)

"""
