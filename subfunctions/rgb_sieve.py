
def rgb_sieve(pixel):
    threshold = 30
    # Вычисляем среднюю яркость пикселя
    average_brightness = (pixel[0] + pixel[1] + pixel[2]) / 3
    
    # Возвращаем True, если средняя яркость меньше порога, иначе False
    return average_brightness < threshold

# def rgb_sieve(pixel):
#     if pixel[0] == 186:
#     # Возвращаем True, если яркость пикселя меньше порога, иначе False
#         return True
#     return False



