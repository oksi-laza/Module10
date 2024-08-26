from threading import Thread
from time import  sleep


class Knight(Thread):
    """
    :param name (str) - имя рыцаря.
    :param power (int) - сила рыцаря.
    """

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} день(дня), осталось {self.enemies} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
