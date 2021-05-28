with open('Req_01.fasta') as f1:
        data_storege = ""
        for line in f1:
                if line.startswith('>'):
                        header=line
                        print(header)
                else:
                        data_storege += line.strip()
return hedear, data_storege

