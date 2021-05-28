# def read_file01(file_name):
#     with open(file_name, "r", encoding="EUC-kr") as raw_file:
#         char_numbers = 0
#         i = 0
#         for line in raw_file:
#             char_numbers += len(line)
#             i += 1
#             print(f"[{i}] character: {line.strip()}, character_length: {len(line)}")
#
#         print(f"\nTotal_character: {char_numbers}")
#     return char_numbers
#     f.close()
#
#
# text = "../Data/Req_01.fasta"
# print(read_file01(text))

# with open("../Data/Req_01.fasta", "r", encoding="EUC-kr") as raw_file:
#     char_numbers = 0
#     i = 0
#     for line in raw_file:
#         if line.find('>'):
#             print("> 있습니다.")
#         else:
#             print("못 찾았어요")
#             print(type(line))
#             print(line)

# def get_groups(seq, group_by):
#     data = []
#     for line in seq:
#         # Here the `startswith()` logic can be replaced with other
#         # condition(s) depending on the requirement.
#         if line.startswith(group_by):
#             if data:
#                 yield data
#                 data = []
#         data.append(line)
#
#     if data:
#         yield data
#
#
# with open('../Data/Req_01.fasta') as f:
#     for i, group in enumerate(get_groups(f, ">"), start=1):
#         print("Group #{}".format(i))
#         print("".join(group))

if line.startswith('>'):
        header=line
        #print header
