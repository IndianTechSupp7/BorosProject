import customtkinter as tk
from PIL import Image

MAIN_PATH = "assets/"

def get_img(path, size):
    return tk.CTkImage(light_image=Image.open(MAIN_PATH + path),
                dark_image=Image.open(MAIN_PATH + path),
                size=size)