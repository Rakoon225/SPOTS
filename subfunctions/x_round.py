

def x_round(image, spot):
    from consts import height, width
    max_element = [-1, 0]

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
                 
            if all(value > 5 for value in pixel):
           
                if y == spot[1]:
                    if x > max_element[0]:
                        max_element = [x,y]
                    


    # image.putpixel((max_element[0],max_element[1]), (0,255,0))  
    return max_element[0]

