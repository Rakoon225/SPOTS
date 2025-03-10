import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog, ttk
from functions.function_photo import function_photo
from functions.function_row import function_row
import consts
from PIL import Image, ImageTk, ImageDraw, ImageFont
import imageio
import os
from tkinter import messagebox
from datetime import datetime
from functions.function_nasa import main


class SinglePhotoWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master, background='#333333')
        self.title("Загрузка одного фото")
        self.geometry("800x900")

        # Место для вывода результата (текст)
        self.result_label = ttk.Label(self, text="", background='#333333', foreground='white')
        self.result_label.pack(pady=20)

        # Место для вывода изображения
        self.image_label = ttk.Label(self)
        self.image_label.pack(pady=20)

        # Кнопка для загрузки фото
        btn_load = ttk.Button(self, text="Загрузить фото", command=self.load_photo)
        btn_load.pack(pady=20)

    def load_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            value, image = self.process_photo(file_path)
            
            info_lines = []
            for i, spot in enumerate(value, 1):  # Начинаем нумерацию с 1
                line = f"Пятно {i}: широта {spot['deg'][0]}, долгота {spot['deg'][1]}"
                info_lines.append(line)

            # Собираем всю информацию в одну строку
            info_text = '\n'.join(info_lines)

            text = f'''
                        радиус: {consts.radius}
                        
                        {info_text}
                    '''
            
            self.result_label.config(text=f"{text}")
            self.display_image(image)

    def process_photo(self, photo_path):
        # Здесь предполагается, что function_photo возвращает tuple (строка, объект изображения PIL)
        value, image = function_photo(photo_path)
        return value, image

    def display_image(self, image):
        # Предположим, что максимальные размеры изображения должны быть 480x580
        max_size = (480, 580)
        image.thumbnail(max_size, Image.LANCZOS)  # Изменение размера изображения
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Сохранить ссылку, чтобы избежать ее удаления сборщиком мусора

class PhotoSeriesWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master, background='#333333')
        self.title("Обработка и анимация серии фото")
        self.geometry("1000x800")
        self.resizable(width=False, height=False)

        # Кнопка для загрузки данных пятен
        self.btn_load = ttk.Button(self, text="Загрузить данные пятен", command=self.load_spot_data)
        self.btn_load.pack(pady=20)

        # Рамка для кнопок, каждая из которых соответствует "пятну"
        self.spot_buttons_frame = ttk.Frame(self)
        self.spot_buttons_frame.pack(pady=10, fill='x', expand=True)

        # Место для отображения GIF
        self.gif_label = tk.Label(self)
        self.gif_label.pack(pady=20)

        # Кнопка закрытия окна
        self.btn_close = ttk.Button(self, text="Закрыть", command=self.destroy)
        self.btn_close.pack(pady=10)

    def load_spot_data(self):
        # Очистка содержимого окна перед загрузкой новых данных
        for widget in self.spot_buttons_frame.winfo_children():
            widget.destroy()
        self.gif_label.configure(image='')  # Очищаем GIF

        # Вызов диалогового окна для выбора файлов
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.png")])
        if file_paths:
            spot_data = function_row(file_paths)  # Предположим, что function_row возвращает данные
            self.process_and_display_images(file_paths, spot_data)

    def process_and_display_images(self, file_paths, spot_data):
        processed_images = self.process_images(file_paths)
        gif_path = self.create_gif(processed_images)
        self.display_gif(gif_path)
        self.create_spot_info_buttons([spot_data])

    def process_images(self, file_paths):
        processed_images = []
        for path in file_paths:
            img = Image.open(path)
            draw = ImageDraw.Draw(img)
            img.save(f"temp_{os.path.basename(path)}")
            processed_images.append(path)
        return processed_images

    def create_gif(self, image_paths):
        gif_path = 'output/animation.gif'
        with imageio.get_writer(gif_path, mode='I', duration=0.5, loop=0) as writer:
            for path in image_paths:
                image = imageio.imread(path)
                writer.append_data(image)
        return gif_path

    def display_gif(self, gif_path):
        frames = self.load_frames(gif_path)
        self.animate_gif(frames, 0)

    def create_spot_info_buttons(self, list_spots):
        for spot_dict in list_spots[0]:
            for key, spot_data in spot_dict.items():
                btn = ttk.Button(self.spot_buttons_frame, text=f"Spot {key}",
                                 command=lambda sd=spot_data: self.open_spot_info(sd))
                btn.pack(pady=5, fill='x')

    def open_spot_info(self, spot_data):
        top = tk.Toplevel(self)
        top.title("Spot Information")
        top.geometry("800x800")
        top.configure(background='#333333')
        top.transient(self)
        my_font = tkfont.Font(size=16)  # Задаём шрифт и размер

        # Центрируем содержимое с помощью sticky='nsew' и установки колонок/строк с весом 1
        top.grid_columnconfigure(0, weight=1)
        top.grid_rowconfigure(0, weight=1)
        top.grid_rowconfigure(1, weight=1)
        top.grid_rowconfigure(2, weight=1)
        top.grid_rowconfigure(3, weight=1)

        tk.Label(top, text=f"Speed: {spot_data['speed']}", bg='#333333', fg='white', font=my_font, anchor='center').grid(row=0, column=0, sticky='nsew')
        tk.Label(top, text=f"Coordinates: {spot_data['px']}", bg='#333333', fg='white', font=my_font, anchor='center').grid(row=1, column=0, sticky='nsew')
        tk.Label(top, text=f"Degrees: {spot_data['deg']}", bg='#333333', fg='white', font=my_font, anchor='center').grid(row=2, column=0, sticky='nsew')

        self.process_spot_images(top, spot_data)

    def process_spot_images(self, parent, spot_data):
        processed_images = []
        for i, img_path in enumerate(spot_data['imgs']):
            img = Image.open(img_path)
            draw = ImageDraw.Draw(img)
            x, y = spot_data['px'][i]
            draw.rectangle([x - 10, y - 10, x + 10, y + 10], outline="red", width=2, fill="green")
            img = img.resize((500, 500), Image.Resampling.LANCZOS)
            temp_path = f'temp_image_{i}.png'
            img.save(temp_path)
            processed_images.append(temp_path)
        gif_path = self.create_gif(processed_images)
        self.display_local_gif(parent, gif_path)

    def display_local_gif(self, parent, gif_path):
        frames = self.load_frames(gif_path)
        gif_label = tk.Label(parent)
        gif_label.grid(row=3, column=0)
        self.animate_local_gif(parent, gif_label, frames, 0)

    def animate_local_gif(self, parent, gif_label, frames, current_frame):
        next_frame = (current_frame + 1) % len(frames)
        gif_label.configure(image=frames[next_frame])
        gif_label.image = frames[next_frame]
        parent.after(300, self.animate_local_gif, parent, gif_label, frames, next_frame)

    def load_frames(self, gif_path):
        frames = []
        img = Image.open(gif_path)
        for i in range(img.n_frames):
            img.seek(i)
            frame = ImageTk.PhotoImage(img.copy().convert('RGBA'))
            frames.append(frame)
        return frames
    def animate_gif(self, frames, current_frame):
        if frames:
            next_frame = (current_frame + 1) % len(frames)
            self.gif_label.configure(image=frames[next_frame])
            self.gif_label.image = frames[next_frame]
            # Повтор анимации с задержкой 300 мс
            self.after(300, self.animate_gif, frames, next_frame)
            
class NasaArchiveWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master, background='#333333')
        self.title("Архив NASA")

        tk.Label(self, text="min: 01.04.2010", background='#333333', foreground='white').pack()
        tk.Label(self, text="max: 30.12.2024", background='#333333', foreground='white').pack()

        # Ввод начальной даты
        tk.Label(self, text="Введите начальную дату (дд.мм.гггг):", background='#333333', foreground='white').pack()
        self.start_day = tk.Spinbox(self, from_=1, to=31, width=3)
        self.start_day.pack()
        self.start_month = tk.Spinbox(self, from_=1, to=12, width=3)
        self.start_month.pack()
        self.start_year = tk.Spinbox(self, from_=2011, to=2030, width=5)
        self.start_year.pack()

        # Ввод конечной даты
        tk.Label(self, text="Введите конечную дату (дд.мм.гггг):", background='#333333', foreground='white').pack()
        self.end_day = tk.Spinbox(self, from_=2, to=31, width=3)
        self.end_day.pack()
        self.end_month = tk.Spinbox(self, from_=1, to=12, width=3)
        self.end_month.pack()
        self.end_year = tk.Spinbox(self, from_=2011, to=2030, width=5)
        self.end_year.pack()

        # Кнопка запроса данных
        btn_submit = tk.Button(self, text="Получить данные", background='#333333', foreground='white', command=self.get_nasa_data)
        btn_submit.pack(pady=20)

    def get_nasa_data(self):
        # Получение данных из Spinbox и формирование списков
        start_date_list = [int(self.start_day.get()), int(self.start_month.get()), int(self.start_year.get())]
        end_date_list = [int(self.end_day.get()), int(self.end_month.get()), int(self.end_year.get())]
        start_date = datetime(start_date_list[2], start_date_list[1], start_date_list[0])
        end_date = datetime(end_date_list[2], end_date_list[1], end_date_list[0])

        if start_date >= end_date:
            messagebox.showwarning("Ошибка", "Начальная дата должна быть раньше конечной даты.")
            return
        try:
            main(start_date_list, end_date_list)
            print(f"Запрос данных от {start_date_list} до {end_date_list}")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при получении данных: {e}")
           
class MainApplication(tk.Frame):
    def __init__(self, master):
        super().__init__(master, background='#333333')
        self.master = master
        self.master.title("Главное окно")
        self.master.geometry("700x800")
        self.init_ui()

    def init_ui(self):
        btn_single_photo = ttk.Button(self, text="Одно фото", command=self.open_single_photo_window)
        btn_single_photo.pack(pady=10)

        btn_photo_series = ttk.Button(self, text="Серия фото", command=self.open_photo_series_window)
        btn_photo_series.pack(pady=10)

        btn_nasa_archive = ttk.Button(self, text="Работать с архивом NASA", command=self.open_nasa_archive_window)
        btn_nasa_archive.pack(pady=10)

        self.pack()

    def open_single_photo_window(self):
        window = SinglePhotoWindow(self)
        window.grab_set()

    def open_photo_series_window(self):
        window = PhotoSeriesWindow(self)
        window.grab_set()

    def open_nasa_archive_window(self):
        window = NasaArchiveWindow(self)
        window.grab_set()


def run_application():
    root = tk.Tk()
    root.title("Главное окно")
    root.geometry("500x600")
    root.configure(background='#333333')

    root.style = ttk.Style()
    root.style.theme_use("clam")
    root.style.configure("TButton", background="#333333", foreground="white", borderwidth=1)
    root.style.configure("TLabel", background="#333333", foreground="white")
    root.style.configure("TEntry", fieldbackground="#555555", foreground="white")

    app = MainApplication(root)
    app.mainloop()

if __name__ == "__main__":
    run_application()
