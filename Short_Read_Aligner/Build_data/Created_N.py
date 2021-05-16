import sys
import re

print(sys.argv)

if __name__ == '__main__':
    file = open('SRR11461738.fasta', 'r')

    lines = file.readlines()
    str_ = ""
    maximum_number = '298'

    for line in lines:
        line_strip = line.strip()

        if line_strip == "":
            continue

        if line_strip[0] == '>':
            print(line_strip)
            numbers = re.findall("\d+",line)
            regular_number = numbers[-1]
            sumnumber = int(maximum_number) - int(regular_number)

            final = ''
            for i in range(sumnumber):
                example = 'N'
                final += example

        else:
            print(line_strip + final)

    with open('SRR11461738.fasta', 'w') as file_2:
        str_ = ""        maximum_number = '298'

        for line in lines:
            line_strip = line.strip()

            if line_strip == "":
                continue

            if line_strip[0] == '>':
                file_2.writelines(line_strip + "\n")
                numbers = re.findall("\d+", line)
                regular_number = numbers[-1]
                sumnumber = int(maximum_number) - int(regular_number)

                final = ''
                for i in range(sumnumber):
                    example = 'N'
                    final += example

            else:
                file_2.writelines(line_strip + final + "\n")
