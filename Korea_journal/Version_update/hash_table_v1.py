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
#  Version      : 0.1
#  Rev. Date    : July. 06, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - matplotlib
#   - pyx : Refer to http://pyx.sourceforge.net
# -----------------------------------------------------------------------------------------------------------

"""TargetFile = open('Ref.fa')
readTF = TargetFile.read()
Tseq = "".join(readTF.split())

def cMers(Tseq, k) :
    kFreq = {}

    for i in range(0, len(Tseq)-k+1) :
        kmer = Tseq[i:i +k]

        if kmer in kFreq:
            kFreq[kmer] += 1
        else:
            kFreq[kmer] = 1

    return kFreq

rf = cMers(Tseq, 3)

print(rf)
"""

import time
import matplotlib.pyplot as plt
import os
import pandas


# k-mer size_splicing
def window_size(local__file_size, local__k_size):
    for i in range(0, len(local__file_size) - (local__k_size - 1)):
        yield local__file_size[i:i + local__k_size]


# matplotlib_figure_drowing
def figure_plot():
    plt.plot([1, 4, 7, 8, 13, 17], 'ro-', [6, 4, 7, 1, 1, 2], 'bs-', )
    plt.show()


def main():
    # speed_check_timer : alignment
    start = time.time()

    # Local_Value
    local__string: str = ''
    local__number: int = 0
    local__k_mer: int = 0

    # Local_array
    __local__ref_length = []
    __local__query_length = []
    __local__query_reverse_length = []

    # file_[i] using open
    file_0 = open("Ref.fa", "r")
    file_1 = open("Query.fa", "r")
    file_2 = open("Query_2.fa", "r")

    # file_inserting_&_check_file_number
    window_size(local__string, local__number)
    local__k_mer: int = int(input('Please insert the length of K-mer?\n'))

    result = window_size(file_0.readline(), local__k_mer)
    result_forward = window_size(file_1.readline(), local__k_mer)
    #result_backward = window_size(file_2.read(), local__k_mer)

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
    print('')

    reference_d = dic_example(__local__ref_length)
    query_forward_d = dic_example(__local__query_length)
    query_reverse_d = dic_example(__local__query_reverse_length)
    print(reference_d)
    print(query_forward_d)
    print(query_reverse_d)
    print("")

    print(reference_d.keys())
    print(reference_d.values())
    print(reference_d.items())
    
    file_0.close()
    file_1.close()
    file_2.close()

    figure_plot()

    end = time.time()
    print('current time :', end - start)


# main_start
if __name__ == "__main__":
    main()
