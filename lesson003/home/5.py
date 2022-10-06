def fi(n):
    l = [1, 0, 1]
    for i in range(1, n):
        l.append(l[len(l) - 1] + l[len(l) - 2])
        l.insert(0, l[1] - l[0])
    return l

l = fi(int(input('Введите число: ')))
print(l)