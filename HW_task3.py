# 3.Написать функцию host_range_ping_tab(), возможности которой основаны на функции
# из примера 2.
# Но в данном случае результат должен быть итоговым по всем ip-адресам,
# представленным в табличном формате (использовать модуль tabulate).
# Таблица должна состоять из двух колонок и выглядеть примерно так:
from tabulate import tabulate
from HW_task2 import host_ping_range


def host_ping_range_tab():
    nodes = host_ping_range()
    print(tabulate(nodes, headers='keys'))


if __name__ == '__main__':
    network_range = []
    host_ping_range_tab()