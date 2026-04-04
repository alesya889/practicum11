line = input()

def linefunc(line):
    """
    The function takes a string
    as an argument, converts the
    string to a list of characters,
    sorts the list, converts the list
    back to a string, and returns
    the resulting string.
    :param line: line1
    :return: line2
    """
    linelst = []

    for smb in line:
        linelst.append(smb)

    linelst.sort()
    lineres = ''

    for smb in linelst:
        lineres += smb

    return lineres

print(linefunc(line))
