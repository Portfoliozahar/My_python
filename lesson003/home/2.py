import random


 
def listt(n):
    list = []
    i = 0
    while i < n:
        list.append(random.randint(0, 10))
        i += 1
    print(list)
    return list


def list2(x):
    l = len(x)
    for i in range(l//2):
        print(x[i]*x[l-1-i])
    if l % 2 != 0:
        print(x[l//2])
              

qq = listt(int(input()))
list2(qq)