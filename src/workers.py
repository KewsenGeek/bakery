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
    # Ответ: я удалю просто функцию отдыха


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



# TODO: Здесь просто добавь функции заказа ингредиентов
class Master(Worker):
    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse):
        super().__init__(age, health, hunger, energy, money, happiness, warehouse)

    def work(self):
        print('Управление')

    def order_ingredients(self, ingredients: list[dict[str, int]]):
        self.warehouse.order_ingredients(ingredients)
        time.sleep(3)
        print('Ингредиенты заказаны')



class Seller(Worker):

    def __init__(self, age, health, hunger, energy, money, happiness, warehouse: Warehouse, baker: Baker):
        super().__init__(age, health, hunger, energy, money, happiness, warehouse)
        self.baker = baker

    def sell(self, stuff_to_sell: dict):
        """
        Метод для продажи товара со склада. Если товара недостаточно, то нужно дать задание пекарю изготовить недостающие товары
        :param stuff_to_sell: {товар: кол-во}
        :return:
        """
        all_stuff: dict = self.warehouse.get_stuff()
        for stuff in stuff_to_sell.keys():
            if stuff not in all_stuff.keys() or all_stuff[stuff] <= stuff_to_sell[stuff]:
                self.baker.work({stuff: stuff_to_sell[stuff] - all_stuff[stuff]})
        
        # По идее, когда весь стафф уже есть, нам бы его продать и удалить из таблички, но в тз такого нету

        pass

