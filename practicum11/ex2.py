numbs = input()
numbslist = numbs.split()
numbslist.remove('3')
print([int(_) for _ in numbslist])
