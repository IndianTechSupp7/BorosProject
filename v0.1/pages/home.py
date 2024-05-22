import customtkinter as tk
from comp.page import Page

class HomePage(Page):
    def __init__(self, master):
        super().__init__(master = master)
        self.grid_anchor(tk.CENTER)


        tk.CTkLabel(master=self, text = "Fő oldal", font=(master.font[0], 20)).place(relx=.5, y = 50, anchor="n")
        # ttk.Frame(master=self, height=10).grid(row=1, column = 0)
        self.label_farme = tk.CTkFrame(master=self, width=150, height=100)
        self.label_farme.grid_propagate(False)
        self.label_farme.grid_anchor(tk.CENTER)
        tk.CTkLabel(master=self.label_farme, textvariable=master.hm, font=(master.font[0], 32)).grid(row=0, column = 0)
        tk.CTkLabel(master=self.label_farme, text = " °C", font=(master.font[0], 32)).grid(row=0, column = 1)
        self.label_farme.grid(row=0, column = 0)
        tk.CTkButton(master=self, text="Szerkesztés", command=lambda : master.go2page("config") if master.auth.user else master.go2page("login")).place(relx=.5, rely=0.9, anchor="s")




