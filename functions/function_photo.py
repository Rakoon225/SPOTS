from subfunctions.function_near import function_near
from subfunctions.determinate_coordinates import determine_coordinates
from subfunctions.load_image import load_image
from subfunctions.design_image import design_image
import consts

from subfunctions.time_decorator import time_decorator


@time_decorator
def function_photo(path):
    image, draw = load_image(path)

    if not consts.radius:
        consts.width = image.width
        consts.height = image.height
        
        from subfunctions.right_left_pixel import right_left_pixel
        consts.radius, consts.centrel_pixel = right_left_pixel(image)

    ls = function_near(image, draw)

    spots = []
    

    for element in ls:
        spots.append({
            "px": element,
            "deg": determine_coordinates(element, image, draw)
        })


    design_image(image, draw, spots)
    image.show()
    
    
    print(f'{path}\n')
    return spots


        




   
