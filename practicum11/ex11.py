numbs = input()
nms = numbs.split()
comm = input('Введите комманду: ')
comm1 = comm[0]
comm2 = comm[1]
res = []
shift = int(comm2) % len(nms)
if (comm1 == 'R') or (comm1 == 'r'):
    res.append(nms[-shift:] + nms[:-shift])
elif (comm1 == 'L') or (comm1 == 'l'):
    res.append(nms[shift:] + nms[:shift])
print(*res)