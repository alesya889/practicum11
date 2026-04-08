line1 = input()
line2 = input()
num1 = int(input('Левый диапазон списка 1: '))
num2 = int(input('Правый диапазон списка 1: '))
list1 = line1.split(' ')
list2 = line2.split(' ')
list12 = []

for ind in range(num1 - 1, num2):
    list12.append(list1[ind])

for el in list12[::-1]:
    list2.append(el)

for el in list12:
    list1.remove(el)

intlst1 = []
intlst2 = []

for _ in list1:
    intlst1.append(int(_))

for _ in list2:
    intlst2.append(int(_))

print(intlst1)
print(intlst2)

