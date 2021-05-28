# 전체 염기서열을 한 줄로 변경한다.
def read_file02(file_name):
    data_storege = ""
    with open(file_name, "r", encoding="EUC-kr") as raw_file:
        for line in raw_file:
            data_storege += line.strip()
    return data_storege


def header_and_seq(file_name):
    with open(file_name) as f1:
        data_storege = ""
        for line in f1:
            if line.startswith('>'):
                header = line
                print(header)
            else:
                data_storege += line.strip()
        print(data_storege)
    return header, data_storege


file_path = 'Req_01.fasta'
header_and_seq(file_path)

print("--------------------")
Result = read_file02(file_path)
print(Result)

length = 20
print("length = 5", end="")
print([Result[i:i+length] for i in range(0, len(Result), length)])

Call = [Result[i:i+length] for i in range(0, len(Result), length)]

print(len(Call))
for x in range(len(Call)):
    input_data = open("split_" + str(x) + ".fasta", "w")
    # input_dat.write(referenceHeader +'\n')
    input_data.write(Call[x])