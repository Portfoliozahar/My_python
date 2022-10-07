from random import randint

def l():
    result = ''
    for i in range(n):
        result += str(randint(0, 9))
    return result

def l2(line):
    list = []
    for item in line:
        if line.count(item) == 1:
            list.append(int(item))
    return list

n= int(input("введите длину списка "))
res =l()
print(f'Неповторяющиеся цифры {res}: {l2(res)}')