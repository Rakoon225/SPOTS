import requests
import time
from bs4 import BeautifulSoup
from calendar import monthrange

def format_date_path(base_path, date_tuple):
    """ Строит путь в формате 'base_path/YYYY/MM/DD/' """
    day, month, year = date_tuple
    return f"{base_path}/{year:04d}/{month:02d}/{day:02d}/"

def date_reached_or_passed(current_date, end_date):
    """ Проверяет, достигнута ли или пройдена конечная дата """
    return (current_date[2] > end_date[2]) or \
           (current_date[2] == end_date[2] and current_date[1] > end_date[1]) or \
           (current_date[2] == end_date[2] and current_date[1] == end_date[1] and current_date[0] > end_date[0])

def next_date(current_date):
    """ Возвращает следующую дату """
    day, month, year = current_date
    days_in_current_month = monthrange(year, month)[1]  # Количество дней в текущем месяце

    if day < days_in_current_month:
        return (day + 1, month, year)  # Переход на следующий день
    elif month < 12:
        return (1, month + 1, year)  # Переход на 1 число следующего месяца
    else:
        return (1, 1, year + 1)  # Переход на 1 января следующего года

def directory_search(session, base_path, file_queue, start_date, end_date):
    """ Выполняет поиск файлов в директориях по датам """

    current_date = start_date
    print(f"\n🟢 Начало поиска с даты: {current_date[0]:02d}-{current_date[1]:02d}-{current_date[2]}\n")

    while not date_reached_or_passed(current_date, end_date):
        current_path = format_date_path(base_path, current_date)
        print(f"📂 Проверяем директорию: {current_path}")

        try:
            response = session.get(current_path)
            if response.status_code == 200:
                print(f"✅ Доступ открыт. Анализируем {current_path}:")
                soup = BeautifulSoup(response.text, "html.parser")


                for el in soup.find_all('a', href=True):
                    link = el['href']
                    if "HMIIC" in link or "4500" in link:
                        full_link = current_path + link
                        file_queue.put((full_link, current_path.split("/")))
                        print(f"🔗 Найден файл: {full_link}")
                        break


            else:
                print(f"🚫 Директория {current_path} недоступна или отсутствует.")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Ошибка запроса: {e}. Ожидание перед повтором.")
            time.sleep(10)  # Ожидание перед повторной попыткой

        # Переход к следующей дате
        current_date = next_date(current_date)

    print("\n🏁 Поиск завершён: достигнут крайний срок.")
    file_queue.put(None)  # Сигнал о завершении работы
