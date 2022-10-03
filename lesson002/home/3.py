n = int(input("Введите число: "))

number = []
s = 0


for n in range(1, n + 1):   
    num = round((1+1/n)**n)      
    number.append(num)
    s = s + num
    
print(number)
print(s)


