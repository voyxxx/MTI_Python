myList = [34, 43, 44, 33, True, False, 'one', 'seven', 'eleven', 'wow']
print(*myList)


print(*myList[:5]) # первые 5 элементов списка
print(*myList[-3:]) # последние 3 элемента списка
print(*myList[1::2]) # каждый второй элемент списка

myList[2] = 'newValue'
print(myList)