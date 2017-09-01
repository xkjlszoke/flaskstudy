import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute('CREATE TABLE posts(title TEXT, description TEXT)')
    c.execute('INSERT INTO posts VALUES ("GOOD", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES ("well", "I\'m well.")')
