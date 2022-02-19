"""Связь с дочерним процессом"""
from subprocess import Popen, PIPE
import chardet


def ping_hosts(address_list):
    for node in address_list:
        args = ["ping", "-c", "4", node]
        PROCESS = Popen(args, stdout=PIPE)
        # print(PROCESS)
        # print()
        # communicate - связь с созданным процессом
        # None – это результат stderr, а это значит, что ошибок не найдено
        DATA = PROCESS.communicate()
        # print(DATA)  # -> вернет кортеж (stdout, stderr)
        # print()
        RESULT = chardet.detect(DATA[0])
        OUT = DATA[0].decode(RESULT['encoding'])
        print(OUT)


if __name__ == '__main__':
    address_list = ['192.168.0.101', '127.0.0.1', '1.1.1.1', 'google.ru']
    print(ping_hosts(address_list))