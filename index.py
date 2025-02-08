import sys
sys.path.insert(0, '/path/to/project')

from functions.function_photo import function_photo
import consts

from PIL import Image, ImageDraw, ImageFont, ImageTk

path = 'assets/IMG_2178.png'
image = Image.open(path)
if image.mode != 'RGB':
        image = image.convert('RGB')

consts.width = image.width
consts.height = image.height

print(consts.width)



function_photo(image)