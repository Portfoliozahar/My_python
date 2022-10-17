
# with open('w.txt', 'r') as data:
#     for line in data:
#         print (list(line.split()))
 
line = '1 2 3 2 5 6 4 5'.split()

res = map(int, line)
res = filter(lambda x: not x%2 , res)
res = list(map(lambda x: (x, x**2), res))
print(res)

# def sel(f,col):
#     return[f(x) for x in col]

# def qwe(f,col):
#     return[x for x in col if f(x)]


# res = sel(int, line)
# res = qwe(lambda x: not x%2 , res)
# res = sel(lambda x: (x, x**2), res)
# print(res)
