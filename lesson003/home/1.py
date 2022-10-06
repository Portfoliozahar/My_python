 
import random


 
def listt(n):
    list = []
    i = 0
    while i < n:
        list.append(random.randint(0, 5))
        i += 1
    print(list)
    return list


def list_sum(l):
    s= 0
    for i in range(0, len(l), 2):
        s += l[i]
    print(s)
    
    
    
qq = listt(int(input()))
list_sum(qq)