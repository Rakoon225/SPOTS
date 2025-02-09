import pprint
from functions.function_photo import function_photo
from subfunctions.speed_operation import speed_operation


def function_row(ls):

    data = {}

    for path in ls:
        data[f'{path}'] = function_photo(path)

    print(speed_operation(data))