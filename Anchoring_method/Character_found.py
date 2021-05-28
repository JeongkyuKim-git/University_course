# 전체 염기서열의 수를 체크, 각 라인의 염기의 수를 체크
def read_file01(file_name):
    with open(file_name, "r", encoding="EUC-kr") as raw_file:
        char_numbers = 0
        i = 0
        for line in raw_file:
            char_numbers += len(line)
            i += 1
            print(f"[{i}] character: {line.strip()}, character_length: {len(line)}")

        print(f"\nTotal_character: {char_numbers}")
    return char_numbers
    f.close()


# 전체 염기서열을 한 줄로 변경한다.
def read_file02(file_name):
    data_storege = ""
    with open(file_name, "r", encoding="EUC-kr") as raw_file:
        for line in raw_file:
            data_storege += line.strip()
    return data_storege


file_path = "../Data/req.txt"
Total_number = read_file01(file_path)
print("--------------------")
Result = read_file02(file_path)

print(Total_number)
print(Result)

length = 5
print("length = 5", end="")
print([Result[i:i+length] for i in range(0, len(Result), length)])

length = 10
print("length = 10", end="")
print([Result[i:i+length] for i in range(0, len(Result), length)])

length = 15
print("length = 15", end="")
print([Result[i:i+length] for i in range(0, len(Result), length)])

Call = [Result[i:i+length] for i in range(0, len(Result), length)]

print(len(Call))
for x in range(len(Call)):
    input_data = open("split_" + str(x) + ".fasta", "w")
    # input_dat.write(referenceHeader +'\n')
    input_data.write(Call[x])