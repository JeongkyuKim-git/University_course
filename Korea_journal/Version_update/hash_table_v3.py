# kr_research

# hash_table__python3.0
# C:\Users\jkkim\PycharmProjects\untitled
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  KRP (Korea Research Paper)
#
#  Author       : Jeongkyu Kim (Dept. of Multimedia Engineering at Dongguk University, Seoul, Korea)
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.3
#  Rev. Date    : July. 09, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - matplotlib
#   - pyx : Refer to http://pyx.sourceforge.net
# -----------------------------------------------------------------------------------------------------------

import os
import sys
import time
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# k-mer size_splicing
def window_size(local__file_size, local__k_size):
    for i in range(0, len(local__file_size) - (local__k_size - 1)):
        yield local__file_size[i:i + local__k_size]


# matplotlib_figure_drowing
def figure_plot():
    plt.plot([1, 4, 7, 8, 13, 17], 'ro-', [6, 4, 7, 1, 1, 2], 'bs-', )
    plt.show()


def figure_chart2():
    y = [3,4,2,10,4,2,3,1]
    x = range(len(y))
    plt.bar(x,y,width=0.7, color="black")
    plt.show()


def Example(key, value): #key랑 value 추가하기
    if key in dict:
        dict.get(key).append(value)
    else:
        dict[key] = [value]


def dic_example(sequence):  # key랑 value 추가하기
    # array_list
    dictionary = {}

    for i, name in enumerate(sequence, 0):

        # print(name,i)
        if name in dictionary:
            dictionary.get(name).append(i)

        else:
            dictionary[name] = [i]

    return dictionary


def main():
    # Local_Value
    local__string: str = ''
    local__number: int = 0
    local__k_mer: int = 0

    # Local_array_list
    __local__ref_length = []
    __local__query_length = []
    __local__query_reverse_length = []

    # file_inserting_&_check_file_number
    window_size(local__string, local__number)
    local__k_mer: int = int(input('Please insert the length of K-mer?\n'))

    result = window_size(file_0.readline(), local__k_mer)
    result_forward = window_size(file_1.readline(), local__k_mer)

    # reference sequence
    for i in result:
        __local__ref_length.append(i)

    # query sequence forward propagation
    for i in result_forward:
        __local__query_length.append(i)

    # query sequence reverse propagation
    result_reverse = file_2.readline()

    comp_dic = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}  # 상보적 염기를 키-값으로 하는 사전을 만든다.
    #print(result_reverse)
    comp_seq = ""
    for s in result_reverse:
        comp_seq += comp_dic[s]
    #print(comp_seq)
    rev_comp_seq = comp_seq[::-1]
    #print(rev_comp_seq)

    result_backward = window_size(rev_comp_seq, local__k_mer)

    for j in result_backward:
        __local__query_reverse_length.append(j)

    # Main_Focus_Starting_print()
    print("--Main Function--",'\n')

    print("Reference short read :", __local__ref_length)
    print("Query short read (Forward) :", __local__query_length)
    print("Query short read (Reverse):", __local__query_reverse_length)
    print("----------------< k-mer (size) >-------------------")
    print("")

    #coco = dict(zip([i for i in range(1, len(__local__ref_length) + 1)], __local__ref_length))
    #dict(enumerate(__local__ref_length, 0))
    #for i, name in enumerate(__local__ref_length, 0):
        #coco = print(name, i)
    #coco = dict(enumerate(__local__ref_length, 0))
    #coco.keys()
    #print(coco.keys())

    reference_d = dic_example(__local__ref_length)
    query_forward_d = dic_example(__local__query_length)
    query_reverse_d = dic_example(__local__query_reverse_length)
    print("Reference dictionary",reference_d)
    print("query_forward dictionary",query_forward_d)
    print("query_reverse dictionary",query_reverse_d)
    print("----------------< dictionary setting >-------------------")
    print("")

    """
    def dictuonary(dic):
        for key, value in dic.items():
            print(f"{key} : {value}")

    dictuonary(reference_d)
    """

    # print(reference_d.keys())
    # print(reference_d.values())
    # print(reference_d.items())
    testset_rf = reference_d
    print(testset_rf)
    # print test..
    Unique_set_f = set(reference_d)
    Unique_set_f2 = set(reference_d)
    Unique_set_qf = set(query_forward_d)
    Unique_set_qr = set(query_reverse_d)

    # Unique RF<-->QF (common_data_set)
    common_reference_set_f = Unique_set_f.intersection(Unique_set_qf)
    print(common_reference_set_f)
    test_ff = Unique_set_f - common_reference_set_f
    test2_ff = reference_d
    [test2_ff.pop(key, None) for key in test_ff]
    print("RF(origin)<-->QF unique >", test2_ff)
    print("")
    print("")
    print("확인된 RF 서열(비교서열 Query_Forward)")
    print("")

    # Unique RF<-->QR (common_data_set)
    common_reference_set_r = Unique_set_f.intersection(Unique_set_qr)
    print("union",common_reference_set_r)
    print("full_reference",Unique_set_f)
    print("----------------< test 1 setting >-------------------")

    test_fr = Unique_set_f - common_reference_set_r
    print("full_minus_union",test_fr)
    print("full_reference_v2",testset_rf)
    print("full_reference_v2", reference_d)
    [testset_rf.pop(key, None) for key in test_fr]
    print("RF<-->QR unique >", testset_rf)
    print("")
    print("")
    print("확인된 RF 서열(비교서열 Query_Forward)")

    print("----------------< Hash-table setting >-------------------")
    print("")

    # Unique QF<-->RF (common_data_set)
    common_query_set_f = Unique_set_f.intersection(Unique_set_qr)
    print(common_query_set_f)

    # Unique QR<-->RF (common_data_set)
    common_query_set_r = Unique_set_f.intersection(Unique_set_qr)
    print(common_query_set_r)

    remove_empty_ff_key = Unique_set_f.difference(Unique_set_qf)
    unique_reference_ffd = reference_d
    [unique_reference_ffd.pop(key, None) for key in remove_empty_ff_key]
    print("Reference_ff unique >", unique_reference_ffd)

    remove_empty_qf_key = Unique_set_qf.difference(Unique_set_f)
    unique_reference_qfd = query_forward_d
    [unique_reference_qfd.pop(key, None) for key in remove_empty_qf_key]
    print("Query_forward unique >", unique_reference_qfd)

    #---------------------------------------------------------------------

    remove_empty_qr_key = Unique_set_qr.difference(Unique_set_f)
    unique_reference_qrd = query_reverse_d
    [unique_reference_qrd.pop(key, None) for key in remove_empty_qr_key]
    print("Query_reverse unique >", unique_reference_qrd)

    #
    # keys = reference_d.keys()
    # for k in keys:
    #    print(k)

    #figure_plot()
    #figure_chart2()
    print("")

# main_start
if __name__ == "__main__":
    # speed_check_timer : alignment
    start = time.time()

    # file_[i] using open
    file_0 = open("Ref.fa", "r")
    file_1 = open("Query.fa", "r")
    file_2 = open("Query_2.fa", "r")

    # file_0 = open("Cryptomonas curvata.fa", "r")
    # file_1 = open("Cryptomonas curvata_1-42761_v1.fa", "r")
    # file_2 = open("Cryptomonas curvata_1-42761_v1.fa", "r")

    main()


    file_0.close()
    file_1.close()
    file_2.close()

    end = time.time()
    current_time = end -start
    print('current time :', current_time)
