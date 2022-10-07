str_line = ''

file_1 = open('001.txt', 'r')
file_2 = open('002.txt', 'r')

while True:
    line1 = file_1.readline()
    line2 = file_2.readline()
    if not line2 or not line1:
        break

    str_line = line1[:-4] + '+ ' + line2
    with open('003.txt', 'a', encoding='utf-8') as file_my:
        file_my.write(f'{str_line}\n')