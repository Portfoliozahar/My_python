
def F(n):
    res = []
    a = 2
    while a * a <= n:
        if n % a == 0:
            res.append(a)
            n //= a
        else:
            a += 1
    if n > 1:
        res.append(n)
    return res

N = int(input("введите натуральное число: "))

print(F(N))