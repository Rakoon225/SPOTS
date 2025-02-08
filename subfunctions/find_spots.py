
from subfunctions.rgb_sieve import rgb_sieve
import math

ls = []

def find_spots(image, draw):
    from consts import height, width, centrel_pixel, radius, size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y)) 
            if rgb_sieve(pixel):
                distance = round( math.sqrt( ( x - centrel_pixel[0] )**2 + ( y - centrel_pixel[1] )**2 ))
                
                if distance+70 < radius: 
                    # draw.rectangle((x, y, x+10, y+10), fill='blue')

                    ls.append([x,y, x+size, y+size])

    return ls