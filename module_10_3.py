from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    """
    :param balance (int) - баланс банка.
    :param lock - объект класса Lock для блокировки потоков.
    """
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            random_number = randint(50, 500)
            self.balance += random_number
            print(f'Пополнение: {random_number}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        sleep(0.001)

    def take(self):
        for i in range(100):
            random_number = randint(50, 500)
            print(f'Запрос на {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                with self.lock:
                    print(f'Запрос отклонён, недостаточно средств')


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')
