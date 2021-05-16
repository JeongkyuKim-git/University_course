"""
# import sys
# import re

if __name__ == '__main__':
    file = open('output_last_v00.bed', 'r')

    lines = file.readlines()

    # initialize lists
    starts = []
    ends = []
    references = []
    queries = []

    # store the necessary data onto lists
    size = range(len(lines))
    for i in size:
      starts.append(lines[i].split()[1])
      ends.append(lines[i].split()[2])
      references.append(lines[i].split()[6])

    # iterate through each query
    # for each query perform:
      # start from end of query string
      # count the number of N instances
      # subtract the resuting number to query's corresponding end
    sizeOfMatching = range(len(lines))
    for i in sizeOfMatching:
      count = 0;
      for chars in reversed(references[i]):
        if chars == 'N':
          count = count + 1
        else:
          break
      print('original-length: ' + ends[i])
      print('number of Ns: ' + str(count))
      ends[i] = int(ends[i]) - count
      print('new-length: ' + str(ends[i]))
      print('\n')
"""
#------------------------------------------------------------------------------------------------------------------------
      # import sys
      # import re

if __name__ == '__main__':

          file = open('output_last_v00.bed', 'r')
          lines = file.readlines()

          appendedFile = open('mismatch-0-appended', 'w')

          # print(lines[0])
          # for line in lines
          totalLines = range(len(lines))
          for i in totalLines:
              print(i)
              if (i % 2) == 0:
                  print(lines[i + 1])
                  appendedFile.write(lines[i].strip() + ' ' + lines[i + 1].strip())
                  appendedFile.write('\n')
          appendedFile.close()

          file = open('mismatch-0-appended', 'r')
          lines = file.readlines()

          # initialize lists
          starts = []
          ends = []
          references = []
          queries = []

          # store the necessary data onto lists
          size = range(len(lines))
          for i in size:
              starts.append(lines[i].split()[1])
              # print(starts[i])
              ends.append(lines[i].split()[2])
              # print(ends[i])
              references.append(lines[i].split()[6])
              # print(references[i])
              queries.append(lines[i].split()[7])
              # print(queries[i])

          # iterate through each query
          # for each query perform:
          # start from end of query string
          # count the number of N instances
          # subtract the resulting number to query's corresponding end
          sizeOfMatching = range(len(lines))
          for i in sizeOfMatching:
              count = 0
              for chars in reversed(queries[i]):
                  if chars == 'N':
                      count = count + 1
                  else:
                      break
              print('original-length: ' + ends[i])
              print('number of Ns: ' + str(count))
              ends[i] = int(ends[i]) - count
              print('new-length: ' + str(ends[i]))
              print('\n')

          # write to new file
          newFile = open('mismatch-0-final.bed', 'w')
          # newFile.write('hello' + '   ' + 'hello')
          # newFile.write('\n')
          # newFile.write('hello')
          # newFile.close()

          for j in sizeOfMatching:
              newFile.write(lines[j].split()[0])
              newFile.write('\t')
              newFile.write(lines[j].split()[1] + '\t')
              newFile.write(str(ends[j]) + '\t')
              newFile.write(lines[j].split()[3])
              newFile.write('\t')
              newFile.write(lines[j].split()[4])
              newFile.write('\t')
              newFile.write(lines[j].split()[5])
              newFile.write('\t')
              newFile.write(lines[j].split()[6] + '\t')
              newFile.write(lines[j].split()[7])
              newFile.write('\n')
          newFile.close()
