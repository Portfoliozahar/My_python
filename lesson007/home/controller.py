import Model
import view


def operation(str, i, oper):
    if str[i] == oper:
        str[i - 1] = Model.acti.get(oper)(int(str[i - 1]), int(str[i + 1]))
        deleteElement(str, i)
        return True
    return False

def deleteElement(string, i):
    string.pop(i)
    string.pop(i)

def calculate(str: str):
    while len(str) > 1:
        for i in range(len(str)):
            if operation(str, i, '^'): break
            
        
        if '*' in str or '/' in str:
            for i in range(len(str)):
                if operation(str, i, '*'): break
                if operation(str, i, '/'): break

        elif '+' in str or '-' in str:
            for i in range(len(str)):
                if operation(str, i, '+'): break
                if operation(str, i, '-'): break
    return str


def expression(exp: str):
    exp = Model.qwe(exp)
    while len(exp) > 1: 
        exp = calculate(exp)
    Model.result = exp[0]
    view.res1()
