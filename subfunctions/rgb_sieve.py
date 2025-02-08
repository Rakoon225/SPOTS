

def rgb_sieve(pixel):
    threshold = 10  # Можно регулировать в зависимости от желаемой чувствительности

    # Проверяем, что все компоненты цвета (R, G, B) больше порога
    if all(color_component > threshold for color_component in pixel):
        return True
    else:
        return False