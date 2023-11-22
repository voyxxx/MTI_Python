import sys

text = 'Введите список чисел через пробел: '

myDict = {
    1: 'первый',
    2: 'второй'
}

def assembleReq(enum): 
    return f'Введите {myDict[enum]} список: '

list1 = list2 = []

for i in myDict.keys():
    try:
        tempList = f'list{i}'
        globals()[tempList] = list(map(int, input(assembleReq(i)).split()))  
    except ValueError:
        print('Введенные данные неверны. Программа будет завершена.')
        sys.exit()

myIntersection = set(list1).intersection(set(list2))
print(f'Количество пересечений: {len(myIntersection)}. Дублирующие значения не учтены.')