"""tabulate - это модуль, который позволяет красиво отображать табличные данные."""
from tabulate import tabulate

# генерация таблицы без шапки
TUPLES_LIST = [('Python', 'interpreted', '1991'),
               ('JAVA', 'compiled', '1995'),
               ('С', 'compiled', '1972')]
print(tabulate(TUPLES_LIST))
print()

# генерация таблицы с шапкой
COLUMNS = ['programming language', 'type', 'year']
print(tabulate(TUPLES_LIST, headers=COLUMNS))

# генерация таблицы с шапкой
# шапка - первый элемент списка
TUPLES_LIST = [('programming language', 'type', 'year'),
               ('Python', 'interpreted', '1991'),
               ('JAVA', 'compiled', '1995'),
               ('С', 'compiled', '1972')]
# Указание первой строки таблицы как набора заголовков
print(tabulate(TUPLES_LIST, headers='firstrow'))
print()

# если данные - список словарей, значение параметра headers является оператор keys
DICTS_LIST = [{'programming language': 'Python',
               'type': 'interpreted',
               'year': '1991'},
              {'programming language': 'JAVA',
               'type': 'compiled',
               'year': '1995'},
              {'programming language': 'С',
               'type': 'compiled',
               'year': '1972'}]
# Табличное представление списка словарей
print(tabulate(DICTS_LIST, headers='keys'))