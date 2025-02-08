from subfunctions.function_near import function_near
from subfunctions.determinate_coordinates import determine_coordinates
from subfunctions.load_image import load_image
import consts


def function_photo(path):
    image, draw = load_image(path)

    consts.width = image.width
    consts.height = image.height

    from subfunctions.right_left_pixel import right_left_pixel
    consts.radius, consts.centrel_pixel = right_left_pixel(image)

    ls = function_near(image, draw)

    for element in ls:
        draw.rectangle((element[0], element[1], element[2], element[3]), fill='blue')
        draw.text((element[0], element[1]), f"{determine_coordinates(element, image)}", fill='black')

    image.save('example.png')


        




   
