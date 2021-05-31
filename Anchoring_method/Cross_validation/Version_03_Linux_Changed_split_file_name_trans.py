import sys

if __name__ == "__main__":

    FILE_INPUT_DATA = str(sys.argv[1])
    FILE_SPLIT_LENGTH = int(sys.argv[2])

    # 전체 염기서열을 한 줄로 변경한다.
    def read_file02(file_name):
        data_storege = ""
        with open(file_name, "r", encoding="EUC-kr") as raw_file:
            for line in raw_file:
                data_storege += line.strip()
        return data_storege


    # header (">" 구분)
    def header(file_name):
        with open(file_name) as f1:
            data_storege = ""
            for line in f1:
                if line.startswith('>'):
                    header = line
        return header


    # "seq 데이터 뽑기"


    def seq(file_name):
        with open(file_name) as f1:
            data_storege = ""
            for line in f1:
                if line.startswith('>'):
                    header = line
                else:
                    data_storege += line.strip()
        return data_storege


    file_path = FILE_INPUT_DATA
    Result = seq(file_path)
    # Result = read_file02(file_path)
    # print(Result)
    


    # length = splicing 하는 길이
    length = FILE_SPLIT_LENGTH

    # Call = 길이에 따라 분기를 함
    Call = [Result[i:i + length] for i in range(0, len(Result), length)]

    print(header(file_path).strip())
    print("--------------------")
    print(f"length = {length}")
    print(" ")
    print(Call)
    #
    # print(header(file_path).strip())

    text = "\n"
    length_check = " (length = %s)" % str(length)
    Replace_name_01 = FILE_INPUT_DATA.replace(".fasta","")
    Replace_name_02 = Replace_name_01.replace("./Dataset","")

    # 파일을 여러개 생성하는 구문
    for x in range(len(Call)):
        input_data = open("Final/" + Replace_name_02 + "_split_" + str(x) + ".fasta", "w")
        # input_dat.write(referenceHeader +'\n')
        input_data.write(header(file_path).strip())
        input_data.write(length_check)
        input_data.write(text)
        input_data.write(Call[x])
