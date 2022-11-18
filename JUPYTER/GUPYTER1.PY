import matplotlib.pyplot as plt
import numpy as np
from sympy import *



x = np.arange(-100, 100, 0.01)

def func(x):
    f= -12 * x**4 * np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
    return f

from sympy import *
import numpy as np

x = Symbol('x')
y = -12 * x**4 * sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

yprime = y.diff(x)
print(yprime)

    

x1 = 0.45
x2 = 3.81
x = 3.81


def qwe(x):
    plt.figure(figsize=(8,7))
    x_range_down = np.arange(-100, x1, 0.01)
    x_range_up = np.arange(x2, 100, 0.01)
    plt.title(f'Корни функции: {x1}, {x2}\n'
              f'В окрестности точки x ={x}\n'
              f'производная функции меняет знак с (+) на (-)\n'
              f'Следовательно, точка x = {x} - вершина')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    plt.plot(x_range_down, func(x_range_down), 'r', label="Убывание")
    plt.plot(x_range_up, func(x_range_up), 'b', label="Возрастание")
    plt.plot(x, func(x), 'ro')
    plt.text(x, func(x) + 100000000, f'Вершина функции \n'
                                     f' x = {x}')
    plt.legend()
    
    plt.show()
    
qwe(x)


