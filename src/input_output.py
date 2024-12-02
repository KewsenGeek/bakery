import re

# Функции проверяющие ввод и вывод. Просто скопируй и вставь в нужное место в коде!
def check_text(inp):
    if re.fullmatch(r'[а-я А-Я]+', inp):
        return inp
    else:
        return 0
    
print('check_text')
print(check_text("Привет мир"))  # Вывод: Привет мир
print(check_text("Hello world"))  # Вывод: 0
print(check_text("Привет123"))  # Вывод: 0
print(check_text("привет")) # Вывод: привет
print(check_text("")) # Вывод: 0
print(check_text("[]")) # Вывод: 0

def check_int(inp):
    try:
        int_value = int(inp)
        return int_value
    except (ValueError, TypeError):
        return 0
    
print('check_int')
print(check_int(10))       # Вывод: 10
print(check_int("10"))     # Вывод: 10
print(check_int("10.5"))   # Вывод: 0
print(check_int("abc"))    # Вывод: 0
print(check_int(10.5))    # Вывод: 0
print(check_int([1,2,3])) # Вывод: 0

def check_float(inp):
    try:
        float_value = float(inp)
        return float_value
    except (ValueError, TypeError):
        return 0

print('check_float') 
print(check_float(10.5))    # Вывод: 10.5
print(check_float("10.5"))  # Вывод: 10.5
print(check_float("10"))    # Вывод: 10.0
print(check_float("abc"))   # Вывод: 0
print(check_float(10))      # Вывод: 10.0
print(check_float([1,2,3])) # Вывод: 0