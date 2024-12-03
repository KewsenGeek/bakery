"""Файл с классом buyer"""


# Названия классов принято называть с большой буквы, чтобы не было путаницы
class Buyer:

    def __init__(self, name=str, age=int, money=int, sex=bool, address=str):
        self.name = name
        self.age = age
        self.money = money
        self.sex = sex
        self.address = address

    """функция проверки хватает ли денег"""

    # на ввод подаётся цена товара. сравнивает кол-во денег клинта и цену товара
    def check_money(self, price):

        if self.money < price:
            print("Найди работу")
        else:
            print("приятно иметь с вами дело")

    """функция проверки достаточно ли взрослый человек"""

    # на ввод подаётся возрастная категория товара (кол-во лет, необходиоме для покупки) сравниавет с возрастом заказчика
    def check_age(self, required_age):

        if self.age < required_age:
            print("возвращайтесь через", required_age - self.age, "лет")
        else:
            print("приятно иметь с вами дело")

#k = buyer(input("имя"),input("возраст"),input("деньги"),input("пол"),input("адрес"))
#k = buyer ("зер", 13,500, "муж", "ван")
#k.check_age(18)
#k.check_money(10000)
