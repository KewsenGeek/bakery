"""Файл с классом Warehouse"""

import sqlite3
import time


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
        self.connection.commit()
        





    def get_staff(self) -> list[dict[str, int]]:
        """
        Возвращает список всех ингредиентов в формате {ингредиент: кол-во}
        :return: list[dict]
        """
        return [{i: j} for i, j in self.cursor.execute("SELECT * FROM Stuff").fetchall()]

    def write_stuff(self, stuff: dict[str, int]) -> None:
        """
        Записывает данные о товарах в базу данных
        Данные принимаются в формате {ингредиент: кол-во}
        :param stuff: dict
        :return:
        """
        for i in stuff.keys():
            self.cursor.execute('INSERT INTO Stuff (name, amount) VALUES (?, ?)', (i, stuff[i]))
        self.connection.commit()

    def order_ingredients(self, ingredients: list[dict[str, int]]) -> None:
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

    def get_ingredients(self) -> list[dict[str, int]]:
        """
        Возвращает список всех ингредиентов в формате {ингредиент: кол-во}
        :return: list[dict]
        """
        return [{i: j} for i, j in self.cursor.execute("SELECT * FROM Ingredients").fetchall()]

class Bakery:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Функция для создания экземпляра класса Bakery
def create_bakery_instance(**attributes):
    return Bakery(**attributes)


# Создание экземпляров класса Bakery
def predefined_bakery_examples():
    # Данные для создания экземпляров
    bakery_items_data = [
        {"name": "Булочка с картошкой", "тесто": 100, "картошка": 50},
        {"name": "сосиска в тесте", "тесто": 100, "сосиска": 45},
        {"name": "Круассан", "тесто": 75},
        {"name": "пицца", "тесто": 150, "колбаса": 80,"помидоры":30},
    ]
     bakery_items = []
    for example in examples:
        bakery_item = create_bakery_instance(**example)
        bakery_items.append(bakery_item)
    
    return bakery_items
# Создаем список экземпляров
bakery_examples = predefined_bakery_examples()

