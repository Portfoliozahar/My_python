import datetime
sec = int(input("Введите время в секундах: "))
res = datetime.timedelta(seconds=sec)
print(res)