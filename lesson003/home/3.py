
import random

n = int(input('чисел в списке: '))
def List():
    list = []
    i = 0
    while i < n:
        list.append(round((random.random() * 10), 2))
        i += 1
    return list

def qwe(list):
    newList = []
    for i in range(len(list)):
        if list[i] % 1 != 0:
            newList.append(list[i] % 1)
    return max(newList) - min(newList)

list = List()
print(list)
print(f'Разница : {qwe(list):.2f}')
