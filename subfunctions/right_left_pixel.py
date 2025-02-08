from consts import height, width
from subfunctions.rgb_sieve import rgb_sieve

def right_left_pixel(image):

    right_pixel = [-1, 0]
    left_pixel = [10**9, 0]
    top_pixel = [0, 10**9]
    bottom_pixel = [0, -1]

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
                 
            if rgb_sieve(pixel):
                if x > right_pixel[0]:
                    right_pixel = [x,y]
                if x < left_pixel[0]:
                    left_pixel = [x,y]
                if y < top_pixel[1]:
                    top_pixel = [x,y]
                if y > bottom_pixel[1]:
                    bottom_pixel = [x,y]

    radius = (width - (width - right_pixel[0]) - left_pixel[0]) // 2
    radius_y = (height - (height - bottom_pixel[1]) - top_pixel[1]) // 2
    centrel_pixel = [left_pixel[0] + radius, top_pixel[1] + radius_y]

    return radius, centrel_pixel

