import random

n = int(input('введите число: '))
l = []

while len(l)<n:
    new = random.randint(-n,n)
    if new not in l:
        l.append(new)
       
        
print(l)    

xy=[]

with open('file.txt', 'r') as data:
    xy = data.read().split("\n")  
    
m=l[int(xy[0])]*l[int(xy[1])]

print(f'Произведение позиций {xy[0]} и {xy[1]} равно {m}')  

 