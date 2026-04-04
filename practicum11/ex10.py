line1 = input()
line2 = input()
num1 = int(input('Левый диапазон списка 1: '))
num2 = int(input('Правый диапазон списка 1: '))
list1 = line1.split(' ')
list2 = line2.split(' ')
list12 = []

for ind in range(num1 - 1, num2 + 1):
    list12.append(list1[ind])

for el in list12[::-1]:
    list2.append(el)

for el in list12:
    list1.remove(el)

print(*list1)
print(*list2)

