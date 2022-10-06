n = int(input())
 
a = ''
 
while n > 0:
    a = str(n % 2) + a
    n = n // 2
 
print(a)