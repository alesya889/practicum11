line = input()
linelst = line.split()
reslst = []

for word in linelst:
    if word.strip('.,?!:;') not in reslst:
        reslst.append(word.strip('.,?!:;'))

print(*reslst)