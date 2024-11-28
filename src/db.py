"""Файл с классом Warehouse"""

import sqlite3


class Warehouse:

    def __init__(self, db_name='warehouse.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Stuff (
            name TEXT NOT NULL,
            amount INTEGER
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Ingredients (
            name TEXT NOT NULL,
            amount INTEGER
            )
            """
        )
        self.cursor.execute("INSERT INTO Ingredients (name, amount) VALUES (?, ?)", ('Сахар', 10))  # 10 кг
        self.connection.commit()

    def get_staff(self):
        return self.cursor.execute("SELECT * FROM Stuff").fetchall()

    def write_stuff(self, stuff: dict):
        for i in stuff.keys():
            self.cursor.execute('INSERT INTO Stuff (name, amount) VALUES (?, ?)', (i, stuff[i]))
        self.connection.commit()

    def order_ingredients(self, ingredients):
        pass

    def get_ingredients(self):
        pass
