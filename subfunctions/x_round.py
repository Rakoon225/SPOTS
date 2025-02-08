

def x_round(image, x_spot):
    from consts import height, width
    max_element = -1

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
                 
            if all(value > 100 for value in pixel):             
                if x == x_spot and x > max_element:
                    max_element = x
                    




    return max_element

