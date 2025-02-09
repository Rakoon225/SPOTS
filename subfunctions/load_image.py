from PIL import Image, ImageDraw, ImageFont, ImageTk
import consts
from subfunctions.time_decorator import time_decorator


@time_decorator
def load_image(path):
    image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    draw = ImageDraw.Draw(image)


    return image, draw