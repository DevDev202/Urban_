# -*- coding: utf-8 -*-

# блоки кода

x_coordinate, y_coordinate = 10, 29

if x_coordinate < 0:
    print('Х меньше нуля')
    result = x_coordinate ** 2 + y_coordinate
else:
    print('Х больше нуля')
    result = x_coordinate - y_coordinate
print('Результат', result)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; } else { printf('Больше нуля\n'); z = x - y; } printf('Получается\n', z)

# вложенные блоки кода

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

# оператор pass

if x_coordinate < 0:
    if y_coordinate > 0:
        result = -x_coordinate + y_coordinate
    else:
        result = -x_coordinate - y_coordinate
else:
    result = x_coordinate + y_coordinate

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if x_coordinate < 0:
    if y_coordinate > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

x_coordinate = 2
y_coordinate = x_coordinate * x_coordinate + 1
is_big = x_coordinate >= 3000

x_coordinate = my_poem[-1]
print(x_coordinate)
my_list = [2, 3, 4, 5, 6]

# reformat кода

x_coordinate, y_coordinate = 3, 8

if x_coordinate == 3:
    print(42)

if x_coordinate < 0:
    if y_coordinate > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')


# названия переменных

count_of_my_pets = 34
if count_of_my_pets > 10:
    print('I need more space for my pets!')

my_favorite_pets_and_birds = ['cat', 'wolf', 'ostrich']
if 'lion' in my_favorite_pets_and_birds:
    print('Wow!')

my_favorite_pets_and_birds = ['cat', 'wolf', 'ostrich']
# но такой стиль используется для названий классов


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
x = 34
y = 43
if x > y:
    print()
z = 9
if z > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

ss = ['cat', 'wolf', 'ostrich']
if 'lion' in ss:
    print('Wow!')
