numbs = input()
nms = numbs.split()
comm = input('Введите комманду: ')
comm1 = comm[0]
comm2 = comm[1]
shift = int(comm2) % len(nms)
res = []
if (comm1 == 'R') or (comm1 == 'r'):
    res = nms[-shift:] + nms[:-shift]
elif (comm1 == 'L') or (comm1 == 'l'):
    res = nms[shift:] + nms[:shift]
resint = [int(_) for _ in res]
print(resint)
