"""Файл с классом buyer"""
class buyer:

    def __init__(self, name, age, money, sex, address):
        self.name = name
        self.age = age
        self.money = money
        self.sex = sex
        self.address = address
#сами функции пропишу после появления каталога

    """функция проверки хватает ли денег"""
    def check_money(money,price):
        price = 10
        if money < price:
           print("Найди работу")
        else:
            print("приятно иметь с вами дело")
        #сравнить деньги покупателя с ценой товара, при нехватке отменить заказ и вывыести ответ покупателю с предложением устроиться на работу
    """функция проверки достаточно ли взрослый человек"""
    def check_age(age, required_age):
        required_age = 18
        if age < required_age:
            print( "вохвращайтесь через", required_age - age, "лет")
        else:
            print("приятно иметь с вами дело")
            
        
        #сравнить категорию товара по вохрасту и возраст покупатля. Если покупатель младше, 
        #то вывести ответ с предложением вернуться через "возрастная категория товара минус возраст покупателя" лет
    
  
