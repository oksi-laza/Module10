from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    """
    word_count - количество записываемых слов
    file_name - название файла, куда будут записываться слова
    """
    with open(file_name, 'a+', encoding='utf-8') as file:
        for number in range(1, word_count + 1):
            file.write(f'Какое-то слово № {number}\n')
            sleep(0.1)
    return f'Завершилась запись в файл {file_name}'


# Вызов функции
time_start_f = datetime.now()  # текущее время до начала выполнения функции

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end_f = datetime.now()        # текущее время после выполнения функции
print(f'Работа функций: {time_end_f - time_start_f}')   # вывод разницы начала и конца работы функций


# Cоздание и запуск потоков
time_start_t = datetime.now()      # текущее время до создания потоков

thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()    # Запускаем потоки
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()    # Контроль окончания работы потоков, для получения результата
thr_2.join()
thr_3.join()
thr_4.join()

time_end_t = datetime.now()        # текущее время после возвращения результата потоками
print(f'Работа потоков: {time_end_t - time_start_t}')   # вывод разницы начала и конца работы потоков
