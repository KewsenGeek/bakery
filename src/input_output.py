import re

# Функции проверяющие ввод и вывод. Просто скопируй и вставь в нужное место в коде!
def check_text(inp):
    if re.fullmatch(r'[а-я А-Я]+', inp):
        return 1
    else:
        return 0


def check_int(inp):
    return isinstance(inp, int)
    

def check_float(inp):
    return isinstance(inp, float)
    
def render_menu():
    print(f'{"-"*30}\nВы стоите в центре пекарни\n{"-"*30}\n⭐ 1.Подойти к кассе\n⭐ 2.Осмотреться\n⭐ 3.Выйти из магазина')
    try:
        vvod = int(input())
        if vvod == 1:
            render_counter()
        elif vvod == 2:
            #Надо будет дописать окружение
            pass
        elif vvod == 3:
            end_game()
        else:
            print('❗Для совершения действия введите цифру из меню❗')
            render_menu()
    except ValueError:
        print('❗Введите целое число!❗')
        render_menu()

def render_counter():
    print(f'{"-"*30}\nПеред вами стоит улыбчивый пекарь\nпоказывая на витрины\n{"-"*30}\n⭐ 1.Купить что-нибудь\n⭐ 2.Осмотреть прилавок\n⭐ 3.Отойти')
    try:
        vvod = int(input())
        if vvod == 1:
            # Магазин
            pass
        elif vvod == 2:
            showcase()
        elif vvod == 3:
            render_menu()
        else:
            print('❗Для совершения действия введите цифру из меню❗')
            render_counter()
    except ValueError:
        print('❗Введите целое число!❗')
        render_counter()

def showcase():
    print(f'{"-"*50}\nВитрина пестрит разнообразной выпечкой: булочки\nс корицей, хрустящие багеты, мягкие крендельки\nи ароматные пирожки c творогом.\n{"-"*50}\n⭐ 1.Отойти')
    try:
        vvod = int(input())
        if vvod == 1:
            render_counter()
        else:
            print('❗Для совершения действия введите цифру из меню❗')
            render_menu()
    except ValueError:
        print('❗Введите целое число!❗')
        render_menu()

def end_game():
    print(f'{"-"*30}\nВы подошли к выходу из пекарни\n{"-"*30}\n⭐ 1.Уйти\n⭐ 2.Вернуться')
    try:
        vvod = int(input())
        if vvod == 1:
            #Вывод попкупок
            pass
        elif vvod == 2:
            render_menu()
        else:
            print('❗Для совершения действия введите цифру из меню❗')
            end_game()
    except ValueError:
        print('❗Введите целое число!❗')
        end_game()

render_menu()