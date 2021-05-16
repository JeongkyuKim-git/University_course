if __name__ == '__main__':

    file = open('mismatch-1-final.bed', 'r')
    lines = file.readlines()

    # appendedFile = open('data/test/appended/example-appended', 'w')
    #
    # totalLines = range(len(lines))
    # for i in totalLines:
    #     if (i % 2) == 0:
    #         appendedFile.write(lines[i].strip() + ' ' + lines[i + 1].strip())
    #         appendedFile.write('\n')
    # appendedFile.close()
    #
    # file = open('data/test/appended/example-appended', 'r')
    # lines = file.readlines()

    borders = []

    # store the necessary data onto lists
    size = range(len(lines))
    for i in size:
        borders.append([lines[i].split()[1], lines[i].split()[2]])

    for border in borders:
        border[0] = int(border[0])
        border[1] = int(border[1])

    borders.sort()
    print(borders)

    newFile = open('mismatch-1-result', 'w')
    overlapped = []
    count = 0
    sum = 0
    for i in range(len(borders) - 1):
        if i == 0:
            overlapped = borders[i]
        if overlapped[0] == borders[i + 1][0]:
            overlapped[1] = max(overlapped[1], borders[i + 1][1])
        elif borders[i + 1][0] <= overlapped[1]:
            overlapped[1] = max(overlapped[1], borders[i + 1][1])
        else:
            print(overlapped)
            sum = sum + (int(overlapped[1]) - int(overlapped[0]))
            newFile.write(str(count) + ': [' + str(overlapped[0]) + ', ' + str(overlapped[1]) + ']')
            newFile.write('\n')
            count = count + 1
            overlapped = borders[i + 1]
    print(overlapped)
    newFile.write(str(count) + ': [' + str(overlapped[0]) + ', ' + str(overlapped[1]) + ']')
    newFile.write('\n')
    newFile.write('\n')
    newFile.write('Total Sum: ' + str(sum))
    newFile.write('\n')
    newFile.write('Sum / Total Length: ' + str(sum / 4212427))
    newFile.close()
