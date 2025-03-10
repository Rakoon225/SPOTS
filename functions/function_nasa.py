import threading
import queue
import requests
import time
from subfunctions.directory_search import directory_search
from subfunctions.process_files import process_files
from subfunctions.time_decorator import time_decorator


@time_decorator
def main(start, end):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    file_queue = queue.Queue()

    thread_search = threading.Thread(target=directory_search, args=(session, "https://sdo.gsfc.nasa.gov/assets/img/browse", file_queue, start, end))
    thread_process = threading.Thread(target=process_files, args=(file_queue,))


    thread_search.start()
    thread_process.start()

    thread_search.join()

    thread_process.join()


