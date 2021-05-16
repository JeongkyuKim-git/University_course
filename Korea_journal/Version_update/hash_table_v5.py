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
#  Version      : 0.5
#  Rev. Date    : July. 10, 2020
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
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns


# k-mer size_splicing
def window_size(local__file_size, local__k_size):
    for i in range(0, len(local__file_size) - (local__k_size - 1)):
        yield local__file_size[i:i + local__k_size]


# matplotlib_figure_drowing
def figure_plot():
    plt.plot([0.19, 0.22, 0.28], 'ro-')
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


def test_set_plot():
    plt.style.use('default')
    sns.set()
    sns.set_style('whitegrid')
    sns.set_palette('Set1')

    x = np.array([0, 2, 4, 6, 8, 10])
    gene_1 = np.array([0, 1.2, 1.3, 1.8, 1.7, 1.5])
    gene_2 = np.array([1, 2.4, 2.3, 2.1, 2.2, 2.1])

    df = pd.DataFrame({
        'x': x, 'gene1': gene_1, 'gene2': gene_2
    })

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot('x', 'gene1', data=df, label='gene 1', marker='o')
    ax.plot('x', 'gene2', data=df, label='gene 2', marker='o')

    ax.legend()
    ax.set_xlabel("reference sequence [bp 120,000]")
    ax.set_ylabel("query sequence [bp 40,000]")
    ax.set_ylim(0, 5)
    ax.set_xlim(0, 15)
    plt.show()


def test_setting():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.title('Alignment [3-mer]')
    ax.set_xlabel("reference sequence [bp 14]")
    ax.set_ylabel("query sequence [bp 12]")

    #np.random.randn(30)
    test_vx1 = (0,1,2)
    test_vy1 = (0,1,2)
    plt.plot(test_vx1,test_vy1, color="r", marker="o", linestyle="-")

    test_vx2 = (0,1,2)
    test_vy2 = (9,10,11)
    plt.plot(test_vx2,test_vy2, color="r", marker="o", linestyle="-")

    test_vx3 = (1,2,3)
    test_vy3 = (1,2,3)
    plt.plot(test_vx3,test_vy3, color="r", marker="o", linestyle="-")

    test_vx4 = (2,3,4)
    test_vy4 = (2,3,4)
    plt.plot(test_vx4, test_vy4, color="r", marker="o", linestyle="-")

    test_vx5 = (6,7,8)
    test_vy5 = (6,7,8)
    plt.plot(test_vx5, test_vy5, color="r", marker="o", linestyle="-")

    test_vx6 = (6,7,8)
    test_vy6 = (10,11,12)
    plt.plot(test_vx6, test_vy6, color="r", marker="o", linestyle="-")

    test_vx7 = (10,11,12)
    test_vy7 = (6,7,8)
    plt.plot(test_vx7, test_vy7, color="r", marker="o", linestyle="-")

    test_vx8 = (3,4,5)
    test_vy8 = (3,4,5)
    plt.plot(test_vx8, test_vy8, color="r", marker="o", linestyle="-")

    test_vx9 = (4,5,6)
    test_vy9 = (4,5,6)
    plt.plot(test_vx9, test_vy9, color="r", marker="o", linestyle="-")

    test_vx10 = (5,6,7)
    test_vy10 = (5,6,7)
    plt.plot(test_vx10, test_vy10, color="r", marker="o", linestyle="-")

    #reverse
    test_vx11 = (5,4,3)
    test_vy11 = (0,1,2)
    plt.plot(test_vx11, test_vy11, color="g", marker="o", linestyle="-")

    test_vx12 = (5,4,3)
    test_vy12 = (9,10,11)
    plt.plot(test_vx12, test_vy12, color="g", marker="o", linestyle="-")

    test_vx13 = (13,12,11)
    test_vy13 = (5,6,7)
    plt.plot(test_vx13, test_vy13, color="g", marker="o", linestyle="-")

    test_vx14 = (14,13,12)
    test_vy14 = (6,7,8)
    plt.plot(test_vx14, test_vy14, color="g", marker="o", linestyle="-")

    test_vx15 = (4,3,2)
    test_vy15 = (8,9,10)
    plt.plot(test_vx15, test_vy15, color="g", marker="o", linestyle="-")

    plt.show()

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
    start = time.time()
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

    print("Reference short read > :")
    print(__local__ref_length)

    print("Query short read (Forward) > :")
    print(__local__query_length)

    print("Query short read (Reverse) > :")
    print(__local__query_reverse_length)
    print("----------------< k-mer (size) >-------------------")
    print("")

    reference_d = dic_example(__local__ref_length)
    reference_trans_d = dic_example(__local__ref_length)
    query_forward_d = dic_example(__local__query_length)
    query_reverse_d = dic_example(__local__query_reverse_length)
    print("Reference dictionary",reference_d)
    print("query_forward dictionary",query_forward_d)
    print("query_reverse dictionary",query_reverse_d)
    print("----------------< Hash-table setting >-------------------")
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

    # print test..
    Unique_set_f = set(reference_d)
    Unique_set_fr = set(reference_d)
    Unique_set_qf = set(query_forward_d)
    Unique_set_qr = set(query_reverse_d)


    def unique_change_data(fix_data, origin_set_data, compared_set_data):
        complement_data = origin_set_data - compared_set_data
        test = fix_data
        [test.pop(key, None) for key in complement_data]
        return test

    def test(fix_data, data, compared_data):
        #교집합을 찾는 문장 code_section
        symmetric_difference = data.intersection(compared_data)
        test_ff = data - symmetric_difference
        test2_ff = fix_data
        totoga = [test2_ff.pop(key, None) for key in test_ff]
        return totoga
    
    """
    # test
    print("RF(origin)")
    print(reference_d)

    # test qf <--> rf
    print("Q_Forward unique > : ")
    C = test(query_forward_d, Unique_set_qf, Unique_set_f)
    print(C)

    # test qr <--> rf
    print("Q_Reverse unique > : ")
    D = test(query_reverse_d, Unique_set_qr, Unique_set_fr)
    print(D)

    print("Reference (origin) > :")
    #Unique RF<-->QF (common_data_set)
    print(reference_d)

    print("Reference (unique reference & query forward) > :")
    gost = test(reference_d, Unique_set_qr, Unique_set_f)
    print("test 중입니다.",gost)

    print("Reference (unique reference & query reverse) > :")
    unique_change_data(reference_d, Unique_set_f, Unique_set_qr)
    """

    print("Reference (unique reference & query forward) > :")
    #Unique RF<-->QF (common_data_set)
    final_reference_qf = unique_change_data(reference_d, Unique_set_f, Unique_set_qf)
    print(final_reference_qf)

    print("Reference (unique reference & query reverse) > :")
    #Unique RF<-->QF (common_data_set)
    final_reference_qr = unique_change_data(reference_trans_d, Unique_set_f, Unique_set_qr)
    print(final_reference_qr)

    # Unique QF<-->RF (common_data_set)
    print("Query_Forward unique > : ")
    final_query_f = unique_change_data(query_forward_d, Unique_set_qf, Unique_set_f)
    print(final_query_f)

    # Unique QR<-->RF (common_data_set)
    print("Query_Reverse unique > : ")
    final_query_r = unique_change_data(query_reverse_d, Unique_set_qr, Unique_set_fr)
    print(final_query_r)

    print("----------------< unique setting >-------------------")

    # keys = reference_d.keys()
    # for k in keys:
    #    print(k)

    #figure_plot()
    #test_set_plot()
    test_setting()


    """
    def test_graph():
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.title('Short_Read_Alignment')
        ax.set_xlabel("reference sequence [bp 120,000]")
        ax.set_ylabel("query sequence [bp 40,000]")
        #plt.text(3.5, 3.0, '평균:2.5')


        # np.random.randn(30)
        test_vx1 = (0, 1, 2)
        test_vy1 = (0, 1, 2)
        plt.plot(test_vx1, test_vy1, color="g", marker="o", linestyle="-")
    """

    #figure_chart2()
    print("")
    end = time.time()
    current_time = end -start
    print('current time :', current_time)
    print("----------------< Speed >-------------------")


# main_start
if __name__ == "__main__":
    # speed_check_timer : alignment
    start = time.time()

    #"""
    #file_[i] using open
    file_0 = open("Ref.fa", "r")
    file_1 = open("Query.fa", "r")
    file_2 = open("Query_2.fa", "r")
    #"""

    """
    file_0 = open("Cryptomonas curvata.fa", "r")
    file_1 = open("Cryptomonas curvata3_85524-128285_v3.fa", "r")
    file_2 = open("Cryptomonas curvata_1-42761_v1.fa", "r")
    """

    #file_1 = open("Cryptomonas curvata_1-42761_v1.fa", "r")
    #file_2 = open("Cryptomonas curvata_1-42761_v1.fa", "r")

    main()

    file_0.close()
    file_1.close()
    file_2.close()

    print("\n","..... Created graph")
    print("----------------< Graph setting Start >-------------------")
