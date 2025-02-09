from pprint import pprint
from functions.function_photo import function_photo
from subfunctions.speed_operation import speed_operation

from subfunctions.time_decorator import time_decorator


@time_decorator
def function_row(ls):

    data = {}

    for path in ls:
        data[f'{path}'] = function_photo(path)

    pprint(data)
    pprint(speed_operation(data))