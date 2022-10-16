from PIL import Image
import os


def jpg_to_png_converter(file, new_name):
    jpg_image = Image.open(file)
    jpg_image.save(f'{new_name}.png')


current_path = os.path.abspath(os.getcwd())
files_in_jpg_format = os.listdir(f"{current_path}\\jpg_files")
for file in files_in_jpg_format:
    jpg_to_png_converter(f"{current_path}\\jpg_files\\{file}", f"{file.replace('.', '')[:-3]}")
