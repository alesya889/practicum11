numbs = input()
numbslist = numbs.split()
sumch = []
sumnch = []

for n in numbslist:
    if int(n) % 2 == 0:
        sumch.append(int(n))
    else:
        sumnch.append(int(n))

print(sum(sumch))
print(sum(sumnch))