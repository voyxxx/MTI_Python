import json
import sqlite3

# Открываем JSON-файл и читаем его содержимое
with open('products.json') as f:
    data = json.load(f)

# Создаем подключение к базе данных SQLite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Пройдемся по данным в JSON-файле и добавим их в таблицу
for item in data:
    title = item['title']
    description = item['description']
    img = item['img']
    old_price = item['old_price']
    price = item['price']

    # Проверим, существует ли строка с тем же значением поля title в таблице
    cursor.execute('SELECT * FROM landing_product WHERE title=?', (title,))
    row = cursor.fetchone()

    # Если строка не существует, добавим ее в таблицу
    if row is None:
        cursor.execute('INSERT INTO landing_product (title, description, img, old_price, price) VALUES (?, ?, ?, ?, ?)', (title, description, img, old_price, price))


# # Зафиксируем изменения в базе данных
conn.commit()

# Закроем курсор и подключение к базе данных
cursor.close()
conn.close()
