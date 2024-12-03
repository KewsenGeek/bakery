"""Файл с классами работников"""
from db import Warehouse
import time


class Worker:
    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse):
        self.age = age
        self.health = health
        self.hunger = hunger
        self.energy = energy
        self.money = money
        self.happiness = happiness
        self.warehouse = warehouse

    def work(self):
        pass

    # TODO: убери дублирующиеся функции из классов. Методы отдыха у троих работников совпадают,
    #  просто пропиши, что они делают при отдыхе, здесь. Либо убери вообще метод отдыха у всех
    def chill(self):
        pass


class Baker(Worker):
    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse):
        super().__init__(age, health, hunger, energy, money, happiness, warehouse)

    def work(self, order={'Круассан': 10, 'Розан': 15}):
        # TODO: необходимо испечь все товары, используя ингредиенты со склада.
        #  Если ингредиентов недостаточно, то заказать их у начальника
        """
        Прием данных в формате {товар: кол-во}
        :param order:
        :return:
        """
        print('Печем')
        time.sleep(10)
        self.warehouse.write_stuff(order)
        print('Все испечено!')

    def chill(self):
        print('Отдых')


# TODO: Здесь просто добавь функции заказа ингредиентов
class Master(Worker):
    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse):
        super().__init__(age, health, hunger, energy, money, happiness, warehouse)

    def work(self):
        print('Управление')

    def chill(self):
        print('Отдых')


class Seller(Worker):

    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse):
        super().__init__(age, health, hunger, energy, money, happiness, warehouse)

    def sell(self, stuff_to_sell):
        """
        Метод для продажи товара со склада. Если товара недостаточно, то нужно дать задание пекарю изготовить недостающие товары
        :param stuff_to_sell: {товар: кол-во}
        :return:
        """
        pass

