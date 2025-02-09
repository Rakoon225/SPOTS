from subfunctions.find_spots import find_spots

dx = 5
from subfunctions.time_decorator import time_decorator


@time_decorator
def function_near(image, draw):

    ls = find_spots(image, draw)

    i = -1
    while i < len(ls)-1:
        i += 1
        current = ls[i]
        # print("\nРаботаю с элементом: ", current)
        for j in range(i+1, len(ls)):
            other = ls[j]
            # print("Сравниваю с элементом: ", other)
            if abs(current[0]-other[0]) < abs(current[0] - current[2]) and abs(current[1]-other[1]) < abs(current[1] - current[3]):
                # print("+")
                ls[i] = [min(current[0], other[0]), min(current[1], other[1]), max(current[2], other[2]), max(current[3], other[3])]
                ls.remove(other)
                i -= 1 
                break
            else:
                # print("-")
                continue

    return ls