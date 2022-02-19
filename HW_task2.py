# 2.Написать функцию host_range_ping() для перебора ip-адресов из заданного
# диапазона. Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.
from ipaddress import ip_network
from HW_task1 import host_ping


def host_ping_range():
    nodes = []
    address = input(f'Enter network address:')
    prefix = input(f'Enter prefix:')
    range = address + '/' + prefix
    subnet = ip_network(address=range)
    broadcast_address = subnet.broadcast_address
    print(f'Subnet mask: {str(subnet)}')
    print(f'Broadcast address: {broadcast_address}')
    hosts = list(subnet.hosts())
    for k in hosts:
        nodes.append(str(k))
    print(f'Nodes addresses: {nodes}')
    return host_ping(nodes)


if __name__ == '__main__':
    host_ping_range()