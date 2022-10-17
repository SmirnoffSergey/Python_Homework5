# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


        # Сжатие данных


path1 = 't1.txt'

with open(path1) as file:
    data = file.readlines()
count = 1
string = ''
for i in data:
    for j in range(len(i)-1):
        if i[j] == i[j+1]:
            count += 1
        else:
            string += str(count) + i[j]
            count = 1
    string += str(count) + i[j+1]

with open('data_compression.txt', 'w') as file:
    file.write(string)


        # Восстановление данных
        

path2 = 't2.txt'

with open(path2) as file:
        recovery_data = ''.join(file.readlines())
list = []
string = ''
for i in range(len(recovery_data)):
    if recovery_data[i].isdigit():
        string += recovery_data[i]
    else:
        list.append([int(string), recovery_data[i]])
        string = ''

data = ''
for i in list:
    for j in range(len(i)-1):
        data += i[j] * i[j+1]
print(data)

with open('data_recovery.txt', 'w') as file:
    file.write(str(data))