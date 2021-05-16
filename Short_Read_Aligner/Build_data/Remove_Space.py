import sys
print(sys.argv)

if __name__ == '__main__':
    file = open('SRR11461738.fasta', 'r')

    lines = file.readlines()

    str_ = ""
    for line in lines:
        line_strip = line.strip()

        if line_strip == "":
            continue

        if line_strip[0] == '>':
            if str_ == "":
                print(line_strip + "\n")
            else:
                print(str_ + "\n")
                print(line_strip + "\n")
                str_ = ""
        else:
            str_ += line_strip
    print(str_)

    with open('SRR11461738.fasta', 'w') as file_2:

        str_ = ""
        for line in lines:
            line_strip = line.strip()

            if line_strip == "":
                continue

            if line_strip[0] == '>':
                if str_ == "":
                    file_2.writelines(line_strip + "\n")
                    print(line_strip + "\n")
                else:
                    file_2.writelines(str_ + "\n")
                    file_2.writelines(line_strip + "\n")
                    print(str_ + "\n")
                    print(line_strip + "\n")
                    str_ = ""
            else:
                str_ += line_strip
        file_2.writelines(str_)
        print(str_)
