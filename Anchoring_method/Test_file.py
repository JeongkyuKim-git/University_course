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


text = 'Req_01.fasta'
header_and_seq(text)
