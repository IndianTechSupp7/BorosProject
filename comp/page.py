import customtkinter as tk

class Page(tk.CTkFrame):
    current = None
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master = master, *args, **kwargs)
        self.grid_propagate(False)

