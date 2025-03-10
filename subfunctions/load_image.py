from PIL import Image, ImageDraw, ImageFont, ImageTk
import requests
from io import BytesIO
from subfunctions.time_decorator import time_decorator


@time_decorator
def load_image(path):
    # Проверяем, является ли path URL (то есть начинается с "http" или "https")
    if path.startswith("http"):
        response = requests.get(path)  # Делаем GET-запрос
        if response.status_code != 200:
            raise ValueError(f"Ошибка загрузки изображения: {path}")

        image = Image.open(BytesIO(response.content))  # Открываем изображение из памяти
    else:
        image = Image.open(path)  # Если это локальный файл, открываем как обычно

    if image.mode != 'RGB':  
        image = image.convert('RGB')  
    # gray_image = image.convert('L')

    draw = ImageDraw.Draw(image)  

    print(f"Загружено изображение {path}, размер: {image.size}")  # Логируем вывод

    return image, draw