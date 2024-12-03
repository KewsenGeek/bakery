"""Основной файл, в котором будет порт ввода/вывода"""

from src.buyer import Buyer
from src.db import Warehouse
from src.input_output import render_menu


def main():

    name = str(input('Введите ваше имя: '))
    age = None
    while not isinstance(age, int):
        try:
            age = int(input('Введите ваш возраст: '))
        except:
            print('Возраст должен быть целым числом!')
    money = None
    while not isinstance(money, int):
        try:
            money = int(input('Сколько у вас денег (округленное целое значение)? '))
        except:
            print('Деньги должны быть целым числом!')
    sex = None
    while not(sex == 'М' or sex == 'Ж'):
        sex = input('Введите ваш пол (М или Ж): ')
        if sex not in ['М', 'Ж']:
            print('Пол должен быть М или Ж!')
    address = input('Введите адрес, куда вам доставить готовую выпечку')

    buyer = Buyer(name, age, money, sex, address)

    render_menu()


if __name__ == '__main__':
    main()
