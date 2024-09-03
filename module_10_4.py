from threading import Thread
from time import sleep
from random import randint
import queue


class Table:
    """
    :param number (int) - номер стола.
    :param guest - гость, который сидит за этим столом.
    """
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    """ :param name (str) - имя гостя. """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    """
    :param tables - столы в этом кафе (любая коллекция).
    :param queue - очередь (объект класса Queue)
    """
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()    # создание очереди

    def guest_arrival(self, *guests):
        """Имитация прибытия гостей"""
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}.')
                    break
            else:    # когда все столы перебрали(закончились), следующие гости в цикле помещаются в очередь
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        """Имитация процесса обслуживания гостей (цикл, пока очередь не пустая или хотя бы один стол занят)"""
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # если стол занят и гость поел(т.е. поток завершил работу)
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла) \nСтол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:   # если очередь не пустая и есть свободный стол
                    table.guest = self.queue.get()    # взяли 'guest' - следующего в очереди
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')
                    table.guest.start()


# Проверка кода
# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей (потоки)
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
