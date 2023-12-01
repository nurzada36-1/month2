import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_data(conn, sql, data):
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_to_create_countries_table = '''
CREATE TABLE IF NOT EXISTS countries(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
'''

sql_insert_countries_data = '''
INSERT INTO countries (title) VALUES (?)
'''
countries_data = [('Кыргызстан',), ('Пекин',), ('Казахстан',)]

sql_to_create_cities_table = '''
CREATE TABLE IF NOT EXISTS cities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
)
'''

sql_insert_cities_data = '''
INSERT INTO cities (title, country_id) VALUES (?, ?)
'''
cities_data = [('Бишкек', 1), ('Пекин', 2), ('Алмата', 3), ('Ош', 1), ('ПЕКИН', 2), ('Астана', 3), ('Талас', 1)]

sql_to_create_students_table = '''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (id)
)
'''

sql_insert_students_data = '''
INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)
'''
students_data = [
    ('Арзыбек', 'Токмомбаев', 1),
    ('Student2', 'Last2', 2),
    ('Student3', 'Last3', 3),
    ('Student4', 'Last4', 4),
    ('Student5', 'Last5', 5),
    ('Student6', 'Last6', 6),
    ('Student7', 'Last7', 7),
    ('Student8', 'Last8', 1),
    ('Student9', 'Last9', 2),
    ('Student10', 'Last10', 3),
    ('Student11', 'Last11', 4),
    ('Student12', 'Last12', 5),
    ('Student13', 'Last13', 6),
    ('Student14', 'Last14', 7),
    ('Student15', 'Last15', 1)
]

connection = create_connection('hw_8.db')
if connection is not None:
    print('Successfully connected to DB!')

    create_table(connection, sql_to_create_countries_table)
    insert_data(connection, sql_insert_countries_data, countries_data)

    create_table(connection, sql_to_create_cities_table)
    insert_data(connection, sql_insert_cities_data, cities_data)

    create_table(connection, sql_to_create_students_table)
    insert_data(connection, sql_insert_students_data, students_data)

    connection.close()

while True:
    connection = create_connection('hw_8.db')
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM cities')
        cities_list = cursor.fetchall()
        print(
            'Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
        for city in cities_list:
            print(f'{city[0]}. {city[1]}')
        selected_city_id = int(input())
        if selected_city_id == 0:
            break
        elif selected_city_id in [city[0] for city in cities_list]:
            cursor.execute('''
                SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                FROM students
                JOIN cities ON students.city_id = cities.id
                JOIN countries ON cities.country_id = countries.id
                WHERE cities.id = ?
            ''', (selected_city_id,))
            students_info = cursor.fetchall()
            for student in students_info:
                print(
                    f'Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}')
        else:
            print("Введен некорректный id города. Повторите ввод.")

        connection.close()
