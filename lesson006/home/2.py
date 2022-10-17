# n = int(input('Введите число: '))
# def f(x):
#     return ((x == 1) and 1) or x * f(x -1)
# l = list( f(i) for i in range(1, n +1))
# print(l)


n = int(input('Введите число: '))
f = lambda x:((x == 1) and 1) or x * f(x -1)
l = list ( f(i) for i in range(1, n +1))
print(l)