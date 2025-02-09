from subfunctions.time_decorator import time_decorator


@time_decorator
def design_image(image, draw, data):

    for element in data:

        deg_ls = element["deg"]
        px_ls = element["px"]

        draw.rectangle((px_ls[0], px_ls[1], px_ls[2], px_ls[3]), fill='blue')
        draw.text((px_ls[0], px_ls[1]), f"{deg_ls}", fill='black')


