import altair as alt 
from pprint import pprint
import os
from subfunctions.time_decorator import time_decorator
from subfunctions.speed_operation import speed_operation



def create_speed_chart(data):
    ls_x = []
    ls_y = []

    # Обход данных и подсчёт средних значений
    for i in range(len(data)):
        ls_deg = data[i][i+1]["deg"]
        res = sum([el[0] for el in ls_deg])
        avg_res = round(res / len(ls_deg))

        ls_x.append(avg_res)
        ls_y.append(data[i][i+1]["speed"])

    # Создание графика
    chart = alt.Chart(alt.Data(values=[{'x': x, 'y': y} for x, y in zip(ls_x, ls_y)])) \
        .mark_point() \
        .encode(
            x='x:Q',  # Количественные значения
            y='y:Q'
        )    
        
    return chart


def create_area_chart(data):
    # Преобразование данных для графика площади
    area_data = []
    for date, entries in data.items():
        for entry in entries:
            x1, y1, x2, y2 = entry['px']
            area = abs((x2 - x1) * (y2 - y1))
            area_data.append({'date': date, 'area': area})
    chart = alt.Chart(alt.Data(values=area_data)).mark_point().encode(
        x='date:T',
        y='area:Q'
    )
    

    
    return chart

def create_count_chart(data):
    # Преобразование данных для графика количества
    count_data = [{'date': date, 'count': len(entries)} for date, entries in data.items()]
    chart = alt.Chart(alt.Data(values=count_data)).mark_bar().encode(x='date:T', y='count:Q')
    return chart

def save_chart_and_log_data(data, chart, directory_suffix, filename_suffix):
    directory_path = f"data/output/"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)
    chart.save(f"{directory_path}/{filename_suffix}.html")
    with open(f"{directory_path}/{filename_suffix}.txt", 'w') as file:
        file.writelines(str(data))
    print(f"Data written to {directory_path}/{filename_suffix}.txt")
    print(f"Chart saved as {directory_path}/{filename_suffix}.html")

def create_graph(data, time_suffix=''):
    area_chart = create_area_chart(data)
    count_chart = create_count_chart(data)
    speed_cahrt = create_speed_chart(speed_operation(data))

    print(time_suffix)

    save_chart_and_log_data(data, area_chart, time_suffix, 'area_chart')
    save_chart_and_log_data(data, count_chart, time_suffix, 'count_chart')
    save_chart_and_log_data(speed_operation(data), speed_cahrt, time_suffix, 'speed_chart')