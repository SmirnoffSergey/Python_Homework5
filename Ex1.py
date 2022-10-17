# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = input('Input some text in Russian: ').split()
for i in text:
    if 'абв' in i:
        text.remove(i)
print(' '.join(text))