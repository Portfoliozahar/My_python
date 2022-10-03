# n = int(input("Введите число: "))
# a = 1
# for i in range(n):
#     a *= i+1
# print(a)

# import datetime


# now = datetime.datetime.today()
# NY = datetime.datetime(2023, 1, 1)
# d = NY-now  
                    
# mm, ss = divmod(d.seconds, 60)
# hh, mm = divmod(mm, 60)

# print('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))

def cou(a1, a2):
    count = 0
    i=0
    while True:
        i = a1.find(a2, i+1)
        if i == 0:
            return count
        count += 1

print(cou('ифшщфшокугшщифрпиищшфкупиифишщкфиаопиф', 'иф')) 