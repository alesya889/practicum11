line = input()
q = int(input('Сколько необходимо минимально букв с отверстями? '))
lstline = line.split()

def cntwordwthhole(lstlits):
    """
    Сounts how many words with holes
    :param lstlits: the original list of words
    :return: quantity
    """
    c = 0

    for word in lstline:

        for el in 'qabdegop':
            if el in word:
                c += 1
                break
    return c

def wordwthhole(lstline, q):
    """
    Returns a list of words with
    holes greater than or equal to q
    :param lstline: the original list of words
    :param q: the number of words
    :return: list of words
    """
    lst = []

    for word in lstline:
        c = 0
        for el in 'qabdegop':
            c += word.count(el)
        if c >= q:
            lst.append(word)
    return lst

print('Количество слов с отверстиями:', cntwordwthhole(lstline))
print(
    'Количество слов без отверстий:',
     len(lstline) - cntwordwthhole(lstline)
)
print(
    f'Список слов, имеющих больше или ровно'
    f' {q} отверстий:', wordwthhole(lstline, q)
)




