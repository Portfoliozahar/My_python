#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('введите x: '))
y = int(input('введите y: '))
z = int(input('введите z: '))

if (not (x or y or z) == (not x and not y and not z)):
    print('True')
else:
    print('false')