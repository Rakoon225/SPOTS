
from subfunctions.x_round import x_round
import math

def determine_coordinates(element, image, draw):
    from consts import centrel_pixel, radius
    parr = x_round(image, element) - centrel_pixel[0]

    try:
        # Аргумент для asin должен быть в диапазоне [-1, 1]
        lat_argument = (centrel_pixel[1] - element[1]) / radius
        long_argument = (element[0] - centrel_pixel[0]) / parr

        if abs(lat_argument) > 1 or abs(long_argument) > 1:
            raise ValueError("Arguments out of domain for asin")

        latitude = math.degrees(math.asin(lat_argument))
        longitude = math.degrees(math.asin(long_argument))

        return [round(latitude), round(longitude)]

    except ValueError as e:
        # В случае ошибки можно вернуть некое дефолтное значение или обработать на свое усмотрение
        print("Error in computing asin: ", e)
        # Возвращаем значения, указывающие на ошибку в расчетах
        return [None, None]


