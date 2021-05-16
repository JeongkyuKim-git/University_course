#readline() --> 1줄을 읽고 그 결과를 리턴해줍니다.
#readlines() --> Line 단위로 텍스트를 읽고 List로 리턴해 줍니다.
#help(SeqIO)

from Bio import SeqIO
import datetime
import time
import os
import sys
import math

from win32ctypes.tests.test_win32cred import handle

current_time = datetime.datetime.now()
print(current_time)
start = time.time()

reference_file = open("sample2.txt", "r")
reference_file2 = open("sample2.txt", "r")

while True:
    line = reference_file.readline()
    if not line: break
    print(line, end='')

print('')

newlist = [line.rstrip() for line in reference_file2.readlines()]
reference_string_data =''
reference_string_data = ("".join(newlist))
print(reference_string_data)

reference_file.close() #file.close
reference_file2.close()

print("\n=============================================================================================")
final_time = (time.time() - start)
print(time.strftime("current time : %H:%M:%S", time.gmtime(final_time)))
print("=============================================================================================")

# k-mer source
"""
    def k_mer(self, local__file_size, local__k_size):
        for i in range(0, len(local__file_size) - (local__k_size - 1)):
            yield local__file_size[i:i + local__k_size]
"""

# file_open source
"""
file = open("/home/mjs/test/TextFile.txt", "r")
strings = file.readlines()
print(strings)
file.close()

file = open("/home/mjs/test/TextFile.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()
"""

