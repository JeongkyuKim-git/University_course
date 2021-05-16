import time
import sys

reference_file = open('../sample.txt', 'r') # file open reference
"""file_value"""

Reference_list = [] # Reference_list = []
k_mer_reference = [] # k-mer splice_window
k_mer_test = [] # k-mer splice_window
"""list_value"""

local__string: str = ''
local__number: int = 0
"""_value"""

k_mer_size:int = int(input('Please input a word:\n'))# input k-mer 'k'
"""input_value"""

start = time.time()


def window_size(local__file_size, local__k_size):
    for i in range(0, len(local__file_size) - (local__k_size - 1)):
        yield local__file_size[i:i + local__k_size]


window_size(local__string, local__number)
result = window_size(reference_file.read(), k_mer_size)

for i in result:
    k_mer_test.append(i)

print(k_mer_test)
"""
for i in range(0, len(Reference_list[0]) - k_mer_size):
    # newItem = posReadSeq(0, ref_l[i:i+k_mer], (i, i+k_mer-1))
    newItem = readSeq(ref_l[i:i + k_mer], i, i + k_mer - 1)
    ref_reads.append(ref_l[i:i + k_mer])
    ref_list.append(newItem)
    
    while True:
    line = reference_file.readline()
    if not line:
        break
    Reference_list.append(line)

print(Reference_list)
print(Reference_list[0])
print(len(Reference_list[0]))

for i in range(0,len(Reference_list[0]),3):
    k_mer_reference.append(Reference_list[0][i:i+3])

print(k_mer_reference)

"""

print('current time :', (time.time() - start))
#----------------------------------------------------------------------------

"""
while True:
    if sequence == reference__1:
        line = reference__1.readline()
        if not line:
            break
        list.append(line)
        print(list)


lines = reference_str.readlines()
size = range(len(lines))

"""