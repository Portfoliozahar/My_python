# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
def f(x):
    return ((x == 1) and 1) or x * f(x -1)
# f = lambda x:((x == 1) and 1) or x * f(x -1)
l = list( f(i) for i in range(1, n +1))
print(l)


# f = lambda x:((x == 1) and 1) or x * f(x -1)
                # это одно и тоже?
# def f(x):
#     return ((x == 1) and 1) or x * f(x -1)