import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    departament TEXT NOT NULL,
    salary REAL
)

''')
connection.commit()

cursor.execute('''
INSERT INTO employees(name,position,departament,salary)
VALUES(?,?,?,?)
''',('John Doe','Software Engineer','Tech',3000.50))

cursor.execute('''
INSERT INTO employees(name,position,departament,salary)
VALUES(?,?,?,?)
''',('Orges Doe','Software Engineer','Tech',3000.50))
connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
UPDATE employees
SET salary = ?
WHERE name = ?
''',('75000.00','Orges Doe')

)

connection.commit()

cursor.execute('''
DELETE FROM employees
WHERE name = ?

''',('John Doe',)
)

connection.commit()

cursor.close()
connection.close()