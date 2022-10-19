import view

s: str = ''
res: int  = 0


acti = {
    "^": lambda x, y: int(x) ** int(y),
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: (int(x) / int(y)) if int(y) != 0 else view.zero(),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}

def qwe(s: str):
    s = s.replace(' ', '').strip()
    s = s.replace('+', ' + ')\
        .replace('^', ' ^ ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    str = s.split()
    return str