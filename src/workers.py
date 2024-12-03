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

    def chill(self):
        pass


class Backer(Worker):
    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse):
        super().__init__(age, health, hunger, energy, money, happiness, warehouse)

    def work(self, order={'Круассан': 10, 'Розан': 15}):
        """
        прием данных в формате {товар: кол-во}
        :param order:
        :return:
        """
        print('Печем')
        time.sleep(10)
        self.warehouse.write_stuff(order)
        print('Все испечено!')

    def chill(self):
        print('Отдых')


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

