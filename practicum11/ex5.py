numbs = input()
numbslist = numbs.split()
dignumbslist = []

for num in numbslist:
    dignumbslist.append(int(num))

print(sum(dignumbslist) / len(dignumbslist))
