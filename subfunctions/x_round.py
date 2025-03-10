from subfunctions.find_round import find_round

def x_round(image, spot):
    import consts
    max_element = [-1, 0]

    if len(consts.round_ls) == 0:
        find_round(image) 
    
    for el in consts.round_ls:       
        if el[1] == spot[1]:
            if el[0] > max_element[0]:
                max_element = [el[0], el[1]]
                    


    # image.putpixel((max_element[0],max_element[1]), (0,255,0))  
    image.putpixel((max_element[0],max_element[1]), (255,0,255))   
    return max_element[0]

