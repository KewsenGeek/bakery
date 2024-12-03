"""Файл с классом Warehouse"""

import sqlite3
import time


class Warehouse:

    def __init__(self, db_name='warehouse.db'):

        self.all_pastry = [
            'Круассаны', 'Розаны', 'Печенье', 'Хлеб', 'Багет'
        ]

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
        self.connection.commit()

    def get_staff(self):
        """
        Возвращает список всех ингредиентов в формате [ингредиент: кол-во]
        :return: list[dict]
        """
        return [{i: j} for i, j in self.cursor.execute("SELECT * FROM Stuff").fetchall()]

    def write_stuff(self, stuff: dict):
        """
        Записывает данные о товарах в базу данных
        Данные принимаются в формате {ингредиент: кол-во}
        :param stuff: dict
        :return:
        """
        for i in stuff.keys():
            self.cursor.execute('INSERT INTO Stuff (name, amount) VALUES (?, ?)', (i, stuff[i]))
        self.connection.commit()

    def order_ingredients(self, ingredients: list[dict]):
        """
        Метод заказа ингредиентов. Для заказа нужно передать нужные ингредиенты в формате
        [{ингредиент: кол-во}, {ингредиент: кол-во}, ...], кол-во в килограммах
        :param ingredients: list[dict]
        :return: None
        """
        for i in ingredients:
            for j in i.keys():
                self.cursor.execute("INSERT INTO Ingredients (name, amount) VALUES (?, ?)", (j, i[j]))
        time.sleep(3)
        print('Ингредиенты заказаны')


    def get_ingredients(self):
        """
        Возвращает список всех ингредиентов в формате [ингредиент: кол-во]
        :return: list[dict]
        """
        return [{i: j} for i, j in self.cursor.execute("SELECT * FROM Ingredients").fetchall()]
