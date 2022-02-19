from ipaddress import ip_network
from subprocess import Popen, PIPE
from ipaddress import ip_address
from tabulate import tabulate


def ping_hosts(hosts_list):
    result = {'available': [], 'not available': []}
    for node in hosts_list:
        try:
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
    host_range_ping_tab(result)
    return result


def ping_host_range(nodes):
    subnet = ip_network('8.8.8.0/29')
    broadcast_address = subnet.broadcast_address
    print(f'Subnet mask: {str(subnet)}')
    print(f'Broadcast address: {broadcast_address}')
    hosts = list(subnet.hosts())
    for k in hosts:
        nodes.append(str(k))
    print(f'Nodes addresses: {nodes}')
    return nodes


def host_range_ping_tab(nodes):
    # columns = ['available', 'not available']
    print(tabulate(nodes, headers='keys'))


if __name__ == '__main__':
    hosts_list = []
    # hosts_list = ['192.168.0.101', '127.0.0.1', '1.1.1.1', 'google.ru']
    ping_host_range(hosts_list)
    ping_hosts(hosts_list)