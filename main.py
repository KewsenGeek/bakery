"""Основной файл, в котором будет порт ввода/вывода"""

from src.buyer import buyer
from src.db import Warehouse
from src.input_output import render_menu


def main():
    render_menu()


if __name__ == '__main__':
    main()
