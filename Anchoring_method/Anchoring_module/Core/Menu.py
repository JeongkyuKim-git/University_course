# Title Research
# C:\User\jkkim\PycharmProjects\Test-Data
# Comment and Annotation [Single #], [Multiple ctrl + /]
# import argparse --> linux --help (user) [arguments parsing]
# Linux manual "python3 [program_name.py] [refernece_name].fasta [query_name].fasta [k-mer size] [output_file_name]"
# -----------------------------------------------------------------------------------------------------------

# import_packages
import datetime
import time

# Write a brief description of what is used in the program
class information:
    info_repeat = "==========================================================\n"
    info_school = "= School        : Dongguk University                     =\n"
    info_start_date = "= Start. Date   : 2021. 02. 05.                          =\n"
    info_rev_date = "= Rev. Date     : 2021. 02. 05.                          =\n"
    info_version = "= Version       : 0.1                                    =\n"
    info_author = "= Author        : Jeongkyu Kim                           =\n"
    info_program = "= Program       : Pychram_Python-3.0                     =\n"
    info_text = "= What_Changed  : 전체적인 구조 수정                        =\n"
    info_algorithm_name = "= Algorithm_name: JK algorithm DNA sequences alignment   =\n"

    def print_out(self):
        return self.info_repeat + self.info_school + self.info_start_date + self.info_rev_date + self.info_version + self.info_author + self.info_program + self.info_text + self.info_algorithm_name + self.info_repeat


# Swich-case how to used data set? single & multiple (SRA)
class data_set_choose:
    def swich_data_set(self,arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda:"default")
        return self.case()

    def case_0(self):
        return "Query1.fasta"

    def case_1(self):
        return "Query2.fasta"

    def case_default(self):
        return "default"


# Function for calling data
class data_call:

    def call_reference(self, data):
        try:
            file_open_rf = open(data, 'r')
            for reference_sequence in file_open_rf:
                print(reference_sequence, end='')
            return reference_sequence
        except:
            print('여기서 reference의 예외처리를 합니다.')
        finally:
            file_open_rf.close()

    def call_query(self, data):
        try:
            file_open_query = open(data, 'r')
            for query_sequence in file_open_query:
                print(query_sequence, end='')
            return query_sequence
        except:
            print('여기서 query의 예외처리를 합니다.')
        finally:
            file_open_query.close()


if __name__ == "__main__":  # __main__

    print("\n" + "현재 시간:", datetime.datetime.now())
    # info = information & Specifying variables for calling classes
    info = information()
    data_choose = data_set_choose()
    input_data = data_call()

    # Call output_print
    print(info.print_out())

    # Swich-case Re sequencing- Reference sequence compare to [SRA (Seqeunce Read Arcaive)] or [Single query.fasta]
    # SRA (num_1), Single query.fasta (num_2)
    # Introducing how to get started program
    print("Please input SRA and Sequence data set is number (Integer 0 - 1)\n" + "0. SRA\n" + "1. Sequence")
    query_choose = int(input("Select a number.\n"))

    # Reference sequence compare to [SRA (Seqeunce Read Arcaive)] or [Single query.fasta]
    # Input the reference_name.fasta
    print("\nPlease input reference.fasta data set ([sequence_name].fasta)")
    reference_choose = str(input("insert data file name.\n"))

    # 시작 시간 저장
    start = time.time()

    print(), input_data.call_reference(reference_choose)
    print(), input_data.call_query(data_choose.swich_data_set(query_choose))

    print("\n" + "프로그램 총 수행 시간:", time.time() - start)