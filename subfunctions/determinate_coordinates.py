
from subfunctions.x_round import x_round
import math

def determine_coordinates(element, image, draw):
    from consts import centrel_pixel, radius
    parr = x_round( image , element ) - centrel_pixel[0]
    
    # рисует паралель
    # draw.line((centrel_pixel[0], element[1], centrel_pixel[0]+parr, element[1]), fill='blue', width=2)
    

    latitude = math.degrees(math.asin((centrel_pixel[1] - element[1]) / radius))
    longitude = math.degrees(math.asin(( element[0] - centrel_pixel[0]) / parr))

    # print(math.asin(( element[0] - centrel_pixel[0]) / parr))
    # print(( element[0] - centrel_pixel[0]))
    # print(parr)

    return [round(latitude), round(longitude)]

