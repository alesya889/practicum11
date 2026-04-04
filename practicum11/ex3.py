line = input()
linelst = line.split()
reslst = []

for word in linelst:
    reslst.append(word.strip('.,?!:;'))

print(*reslst)