# 1.Написать функцию host_ping(), в которой с помощью утилиты ping будет
# проверяться доступность сетевых узлов. Аргументом функции является список,
# в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом
# соответствующего сообщения («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
from subprocess import Popen, PIPE
from ipaddress import ip_address
from socket import gethostbyname


def host_ping(host_list):
    result = {'available': [], 'not available': []}
    for node in host_list:
        try:
            node = gethostbyname(node)
            node = ip_address(node)
            print(f'Pinging:', node)
        except ValueError:
            continue
        args = ["ping", "-c", "2", "-w", "2", f"{node}"]
        process = Popen(args, stdout=PIPE)
        process.wait()
        print("OK")
        if process.returncode == 0:
            result['available'].append(str(node))
        else:
            result['not available'].append(str(node))
    print(result)
    return result


if __name__ == '__main__':
    hosts_list = ['192.168.0.101', '127.0.0.1', '1.1.1.1', 'google.ru']
    host_ping(hosts_list)