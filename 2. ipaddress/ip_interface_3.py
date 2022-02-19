"""Python для сетевых инженеров"""

# создание объектов IPv4Interface или IPv6Interface
from ipaddress import ip_interface, ip_network

# Функция ipaddress.ip_interface() позволяет создавать
# объект IPv4Interface или IPv6Interface соответственно
IPV4_INT = ip_interface('10.0.1.1/24')

# получение адреса, маски, сети интерфейса
print('IPv4:', IPV4_INT.ip)
print('Netmask:', IPV4_INT.netmask)
print('Network:', IPV4_INT.network)


def ip_network_check(ip_addr):
    """Проверка, является ли адрес адресом сети или хоста"""
    try:
        ip_network(ip_addr)
        print('is network address')
    except ValueError:
        print('is host address')

# проверка типа адреса
IP_2 = '10.0.1.0/24'
ip_network_check(IPV4_INT)
ip_network_check(IP_2)
