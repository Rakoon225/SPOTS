from functions.function_photo import function_photo 
from pprint import pprint
from subfunctions.time_decorator import time_decorator
from subfunctions.create_graph import create_graph
import os
clear = lambda: os.system('cls')

times = 0
data = {}


def process_files(file_queue):
    global times, data

    while True:
        file_info = file_queue.get()

        # Обработка сигнала о завершении
        if file_info is None:
            print("Получен сигнал завершения")
            print("Создание графиков")
            create_graph(data, f'0/0/0')  # Предполагаю, что create_graph корректно умеет обрабатывать дату '0/0/0'
            file_queue.task_done()
            break

        # Обработка файла
        file_path = file_info  
        print(f"Обработка файла {file_path}")
        times += 1
        print('*' * times)
        print(times)

        try:
            data[f'{file_path[1][-4]}/{file_path[1][-3]}/{file_path[1][-2]}'], _ = function_photo(file_path[0])
        except Exception as e:
            create_graph(data, f'0/0/0')
            print(f"😢 Ошибка! Произошла ошибка при обработке файла:\n\t{file_path}\n\tОшибка: {e}")


        file_queue.task_done()

