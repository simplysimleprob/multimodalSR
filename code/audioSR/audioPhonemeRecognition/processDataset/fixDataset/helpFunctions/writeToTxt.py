import os


def writeToTxt(lines, path):
    if (not os.path.exists(os.path.dirname(path))):
        os.makedirs(os.path.dirname(path))
    file = open(path, 'w')
    for line in lines:
        writeLine(lines, line, file)
    file.close()


def writeLine(lines, line, file):
    # don't write newline after last element
    if (lines.index(line) < len(lines) - 1):
        writeNewLine = True
    else:
        writeNewLine = False

    # if a line is a list, there are several elements you want to write on that line. need to convert to str before writing
    if isinstance(line, list) or isinstance(line, tuple):
        line = ' '.join(map(str, line))

    if writeNewLine:
        file.write("%s\n" % line)
    else:
        file.write("%s" % line)


    # phn_labels = [['0', ' ', '2180', ' ', 38], ['2180', ' ', '2740', ' ', 29], ['2740', ' ', '5480', ' ', 5], ['5480', ' ', '7352', ' ', 18], ['7352', ' ', '8647', ' ', 1], ['8647', ' ', '9320', ' ', 19], ['9320', ' ', '11800', ' ', 0], ['11800', ' ', '12680', ' ', 19], ['12680', ' ', '14920', ' ', 5], ['14920', ' ', '16280', ' ', 34], ['16280', ' ', '18640', ' ', 1], ['18640', ' ', '19880', ' ', 20], ['19880', ' ', '20800', ' ', 31], ['20800', ' ', '22440', ' ', 4], ['22440', ' ', '23561', ' ', 37], ['23561', ' ', '25400', ' ', 3], ['25400', ' ', '26770', ' ', 38], ['26770', ' ', '26970', ' ', 28], ['26970', ' ', '27720', ' ', 4], ['27720', ' ', '28600', ' ', 19], ['28600', ' ', '29702', ' ', 0], ['29702', ' ', '31122', ' ', 20], ['31122', ' ', '33050', ' ', 33], ['33050', ' ', '34631', ' ', 7], ['34631', ' ', '35676', ' ', 38], ['35676', ' ', '37160', ' ', 1], ['37160', ' ', '38680', ' ', 38], ['38680', ' ', '39710', ' ', 29], ['39710', ' ', '40160', ' ', 5], ['40160', ' ', '41520', ' ', 38], ['41520', ' ', '41680', ' ', 24], ['41680', ' ', '43320', ' ', 0], ['43320', ' ', '44699', ' ', 38], ['44699', ' ', '46120', ' ', 8], ['46120', ' ', '47130', ' ', 38], ['47130', ' ', '47560', ' ', 30], ['47560', ' ', '48319', ' ', 4], ['48319', ' ', '49294', ' ', 18], ['49294', ' ', '50300', ' ', 38], ['50300', ' ', '51080', ' ', 28], ['51080', ' ', '51773', ' ', 13], ['51773', ' ', '53764', ' ', 0], ['53764', ' ', '55080', ' ', 38], ['55080', ' ', '55271', ' ', 29], ['55271', ' ', '57340', ' ', 38], ['57340', ' ', '58652', ' ', 1], ['58652', ' ', '60114', ' ', 14], ['60114', ' ', '62120', ' ', 7], ['62120', ' ', '62600', ' ', 26], ['62600', ' ', '64458', ' ', 1], ['64458', ' ', '65670', ' ', 38], ['65670', ' ', '67592', ' ', 38], ['67592', ' ', '68690', ' ', 33], ['68690', ' ', '70013', ' ', 6], ['70013', ' ', '70760', ' ', 13], ['70760', ' ', '72180', ' ', 33], ['72180', ' ', '73309', ' ', 1], ['73309', ' ', '74855', ' ', 13], ['74855', ' ', '76124', ' ', 18], ['76124', ' ', '76926', ' ', 4], ['76926', ' ', '77505', ' ', 19], ['77505', ' ', '79325', ' ', 38], ['79325', ' ', '79826', ' ', 29], ['79826', ' ', '81920', ' ', 38]]
    # dst = './test.txt'
    # writeToTxt(phn_labels,dst)



    ## Old version, doesn't work for nested lists
    # def writeToTxt(lines, path):
    #     if (not os.path.exists(os.path.dirname(path))):
    #         os.makedirs(os.path.dirname(path))
    #     file = open(path, 'w')
    #     for line in lines:
    #         if (lines.index(line) < len(lines) - 1):
    #             file.write("%s\n" % line)
    #         else:
    #             file.write("%s" % line)
    #     file.close()
