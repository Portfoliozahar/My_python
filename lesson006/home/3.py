a = list (input('Введите через пробел: ').split())
b = list (input('Введите через пробел: ').split())

# for i in range(4):
#     print(a[i],b[i])
    
res=zip(a,b)
print(list(res))
