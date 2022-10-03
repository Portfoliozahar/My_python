import random

n = int(input('введите число: '))
l = []

while len(l)<n:
    new = random.randint(-n,n)
    if new not in l:
        l.append(new)
        

print(l) 

newl=[]

i=0

while i < len(l):
    index = random.choice(range(len(l)))
    newl.append(l[index])
    l.pop(index)

print(newl)    

       
        
        
# random.shuffle(l)
# print(l)
