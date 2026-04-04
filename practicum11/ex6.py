num = int(input())
dellist = []

for n in range(1, num+1):
    if num % n == 0:
        dellist.append(n)

print(*dellist)
