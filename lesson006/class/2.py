from multiprocessing.dummy import active_children


string = input('Введите выражение: ')

acti = {
    "^": lambda x, y: float(x) ** float(y),
    "*": lambda x, y: float(x) * float(y),
    "/": lambda x, y: float(x) / float(y),
    "+": lambda x, y: float(x) + float(y),
    "-": lambda x, y: float(x) - float(y)}

string = string.replace(' ', '').strip()
string = string.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('^', ' ^ ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')
string = string.split()

def deleteElement(string, i):
    string.pop(i + 1)
    string.pop(i)

def operation(string, i, oper):
    if string[i] == oper:
        string[i - 1] = acti.get(oper)(float(string[i - 1]), float(string[i + 1]))
        deleteElement(string, i)
        return True

example = ''.join(string)

while len(string)>1:
    if '^' in string:
        for i in range(len(string)):
            if operation(string, i, '^'): break
            
    if '*' in string or '/' in string:
        for i in range(len(string)):
            if operation(string, i, '*'): break
            if operation(string, i, '/'): break

    elif '+' in string or '-' in string:
        for i in range(len(string)):
            if operation(string, i, '+'): break
            if operation(string, i, '-'): break

print(f'{string[0]}')
print(eval(example))