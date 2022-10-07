from decimal import Decimal
n = Decimal(input('введите число: '))
d = input('точность округления "0.(0)1"  ')
print(n.quantize(Decimal(d)))



