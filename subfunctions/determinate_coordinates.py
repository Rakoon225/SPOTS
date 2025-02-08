
from subfunctions.x_round import x_round

import math

def determine_coordinates(element, image):
    from consts import centrel_pixel, radius
    parr = abs(2*(centrel_pixel[0] - x_round( image , element[0] )))

    latitude = math.degrees(math.asin((centrel_pixel[1] - element[1]) / radius))
    longitude = math.degrees(math.asin(( element[0] - centrel_pixel[0]) / parr))

    

    return round(latitude), round(longitude)

