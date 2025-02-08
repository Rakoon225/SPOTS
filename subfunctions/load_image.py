from PIL import Image, ImageDraw, ImageFont, ImageTk
import consts

def load_image(path):
    image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    draw = ImageDraw.Draw(image)

    return image, draw