import consts


def find_round(image):
    for y in range(consts.height):
            for x in range(consts.width):
                pixel = image.getpixel((x, y))
                    
                if all(value > 5 for value in pixel):
                    consts.round_ls.append([x,y])           
    return True