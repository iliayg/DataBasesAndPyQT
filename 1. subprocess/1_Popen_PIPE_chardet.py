"""Дочерний процесс запуска консольной команды"""

from subprocess import Popen, PIPE
import chardet

# Класс subprocess.Popen - Выполняет программу в новом процессе
# Popen не дожидается конца выполнения вызванного процесса
# (он завершается, а запущенное приложение 'висит')

# stdin и stdout это файлоподобные объекты, предоставляемые OS.
# stdout=PIPE - стандартный поток вывода
# вывод результатов выполнения команды с декодированием
# мы знаем, что декодировать нужно в cp866
# shell=True - выполнение кода через оболочку
PROC = Popen("ls", shell=True, stdout=PIPE)
print(PROC)
OUT = PROC.stdout.read().decode('utf-8')
print(OUT)

# мы не знаем в чем нужно декодировать
# но нам помогает модуль chardet
PROC = Popen("ls", cwd="..", stdout=PIPE)
DATA = PROC.stdout.read()
RESULT = chardet.detect(DATA)
print(RESULT)
OUT2 = DATA.decode(RESULT['encoding'])
print(OUT2)

# Popen поддерживает менеджеры контекста
with Popen("pwd", stdout=PIPE) as p:
    OUT3 = p.stdout.read().decode('utf-8')
    print(OUT3)
