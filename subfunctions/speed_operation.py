

def speed_operation(dct):
    list_spots = []
    count = 1

    keys = list(dct.keys())
    for key_i in range(len(keys) - 1):
        current_key = keys[key_i]  # Берём текущий ключ (путь к изображению).
        for i in range(len(dct[current_key])):  
            current = dct[current_key][i]["deg"]  

            other_list = [[current[0], current[1]]]
            px_list = [[dct[current_key][i]["px"][0], dct[current_key][i]["px"][1]]]
            imgs_list = [current_key]
            times = 1  # Счётчик совпадений.

            for key_j in range(key_i + 1, len(keys)):
                next_key = keys[key_j]
                for j in range(len(dct[next_key]) - 1, -1, -1): 
                    other = dct[next_key][j]["deg"]

                    if (keys.index(imgs_list[-1]) + 1 == keys.index(next_key)) and \
                    (abs(other_list[-1][0] - other[0]) < 0.5) and \
                    (other_list[-1][1] < other[1]) and \
                    (abs(other_list[-1][1] - other[1]) > 5):

                        other_list.append([other[0], other[1]])
                        px_list.append([dct[next_key][j]["px"][0], dct[next_key][j]["px"][1]])
                        imgs_list.append(next_key)

                        times += 1
                        dct[next_key].pop(j) 

            if times >= 3:
                list_spots.append({
                    count: {
                        "speed": round((abs(other_list[0][1] - other_list[-1][1]) / (times-1)), 2),  # Пример фиксированного значения.
                        "px": px_list,  
                        "deg": other_list,  
                        "imgs": imgs_list  
                    }
                })
                count += 1 
    return list_spots
