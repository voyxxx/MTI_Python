path = '' # Здесь может быть путь к вашему файлу

# из условия неясно надо ли проверять на существование файла, поэтому создам через режим 'w'
file = open(f'{path}sample.txt', 'w')
file.write('Module 2, lesson 5')
file.close()

file = open(f'{path}sample.txt', 'r')
print(file.read())