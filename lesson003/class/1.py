import re

async def check1():
    list1 = ('wgewegew','gwe2gerj','wrhjeri2')
    check = "2"
    rx = re.compile('\d+')         # <- добавлено
    if check in rx.findall(list1): # <- изменено
        print("число 2 найдено!")
    else:
        print("2 не найдено")