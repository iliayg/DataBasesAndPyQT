from sys import exit, platform
from ipaddress import ip_address, IPv4Address, IPv6Address
from asyncio import set_event_loop, run, gather, create_subprocess_shell, subprocess  #, ProactorEventLoop
from tabulate import tabulate
from itertools import repeat


def ProactorEventLoop():
    pass


class AsyncPingHosts:
    # Инициализация кросс-платформенной асинхронной пинг-машины
    def __init__(self, addresses):
        # пингуемые адреса
        self.addresses = addresses
        # доступные из них
        self.reachable = list()
        # недоступные
        self.unreachable = list()

        self._set_addresses_type()

    # Установить тип адресов в  значение ipaddress.IPv4Address или ipaddress.IPv6Address,
    # если в качестве аргумента адресов указан список.
    # sys.exit (1) - выход, если перехвачено исключение ValueError.
    def _set_addresses_type(self):
        try:
            if self._is_addresses_is_list():
                self.addresses = [self._set_address_type(address) for address in self.addresses]
        except ValueError as error:
            print(error)
            exit(1)

    # Валидация объекта - список адресов.True, если переданный объект является списком,
    # иначе вывести ValueError
    def _is_addresses_is_list(self):
        if type(self.addresses) is list:
            return True
        raise ValueError(f'Passed addresses must be a list type. {type(self.addresses)} given.')

    # Установите тип адреса ipaddress.IPv4Address или ipaddress.IPv6Address
    @staticmethod
    def _set_address_type(address):
        if not type(address) in (IPv4Address, IPv6Address):
            try:
                address = ip_address(address)
            except ValueError as error:
                print(error)
                exit(1)
        return address

    # Межплатформенный асинхронный пинг хоста.
    def ping_hosts(self):
        print('Пожалуйста, подождите, пока не закончится пинг. '
              'Нужно около 5 сек если все адреса доступны, '
              'в противном случае около 20 секунд или более, '
              'в зависимости от количества переданных адресов.')
        try:
            if platform == 'win32':
                # Обратите внимание, что в Windows вы должны установить
                # цикл обработки событий в ProactorEventLoop
                loop = ProactorEventLoop()
                # запуск цикла обработки событий
                set_event_loop(loop)
                loop.run_until_complete(self._async_ping())
                loop.close()
            else:
                run(self._async_ping())
        except Exception:
                print("error")

    # Получить задачи и запускать их одновременно
    async def _async_ping(self):
        tasks = (self._ping_host(str(address)) for address in self.addresses)
        await gather(*tasks)

    # Проверить связь с хостом и добавьте его в список
    # доступных или недоступных на основе кода возврата из подпроцесса.
    async def _ping_host(self, address):
        ping_key = self._get_ping_key()
        proc = await create_subprocess_shell(
            f'ping {ping_key} 4 {address}', stdout=subprocess.DEVNULL
        )
        await proc.communicate()
        if proc.returncode == 0:
            self.reachable.append(address)
        else:
            self.unreachable.append(address)

    # Получить ключ для команды ping,
    # которая устанавливает количество отправляемых пакетов.
    @staticmethod
    def _get_ping_key():
        key = '-c'
        if platform == 'win32':
            key = '/n'
        return key

    def get_ping_status_table(self):
        """Получить таблицу с адресами и их статусами."""
        headers = ['Address', 'Status']
        reachable = list(zip(self.reachable, repeat('reachable')))
        unreachable = list(zip(self.unreachable, repeat('unreachable')))
        return tabulate(reachable + unreachable, headers, tablefmt="github")


# создаем объекты адресов
if __name__ == '__main__':
    FROM_ADDR = ip_address('10.0.0.1')
    TO_ADDR = ip_address('10.0.0.15')

    # диапазон пингуемых адресов
    ADDRESSES = [FROM_ADDR + i for i in range(int(TO_ADDR) - int(FROM_ADDR) + 1)]
    ping = AsyncPingHosts(ADDRESSES)
    ping.ping_hosts()
    print(ping.get_ping_status_table())
