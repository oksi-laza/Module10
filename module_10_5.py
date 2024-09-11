from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while f.readline():
            string = f.readline()
            all_data.append(string)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start = datetime.now()
# for filename in filenames:
#     read_info(filename)
# end = datetime.now()
# print(f'Линейный подход: {end - start}')    # примерно 0:00:03.593118


# Многопроцессный
if __name__ == '__main__':
    with Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)

    end = datetime.now()
    print(f'Многопроцессный подход: {end - start}')    # примерно 0:00:01.942822
