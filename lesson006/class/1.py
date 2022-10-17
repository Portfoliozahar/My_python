a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

m=max(a,b)
while True:
    if m%a==0 and m%b==0:
        print(m)
        break
    else:
        m+=1   