from subfunctions.rgb_sieve import rgb_sieve
from consts import height, width

print(width)

def function_photo(image):
    
    
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            new_color = (0,0,255)    
                
            if rgb_sieve(pixel):
                image.putpixel((x, y), new_color)
    
    image.show()