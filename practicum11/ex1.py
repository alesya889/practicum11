numb = input()
numblist = numb.split()
resnums = []

for n in range(1, len(numblist) - 1):
    newelement = int(numblist[n - 1]) + int(numblist[n + 1])
    resnums.append(newelement)

print(resnums)