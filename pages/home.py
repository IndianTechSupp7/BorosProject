import customtkinter as tk
from comp.page import Page
from comp.core_func import get_img
from comp.button import Button
from comp.drawer import Drawer

class HomePage(Page):
    def __init__(self, master):
        super().__init__(master = master)
        self.grid_anchor(tk.CENTER)


        self.menu = tk.CTkLabel(master=self, text="", image=get_img("more.png", (27, 27)))
        self.menu.place(x = 10, y = 10)
        self.drawer = Drawer(master=self)
        # tk.CTkLabel(master=self, text="", image=get_img("tempalte.png", (300, 300*0.6510172143974961))).place(x=0, y=0)
        tk.CTkLabel(master=self, text = "Fő oldal", font=(master.font[0], 20)).place(relx=.5, y = 50, anchor="n")
        # ttk.Frame(master=self, height=10).grid(row=1, column = 0)
        self.label_farme = tk.CTkFrame(master=self, width=150, height=100)
        self.label_farme.grid_propagate(False)
        self.label_farme.grid_anchor(tk.CENTER)
        tk.CTkLabel(master=self.label_farme, textvariable=master.hm, font=(master.font[0], 32)).grid(row=0, column = 0)
        tk.CTkLabel(master=self.label_farme, text = " °C", font=(master.font[0], 32)).grid(row=0, column = 1)
        self.label_farme.grid(row=0, column = 0)
        Button(master=self, text="Szerkesztés", command=lambda : master.go2page("config") if master.auth.user else master.go2page("login")).place(relx=.5, rely=0.9, anchor="s")
        self.menu.bind("<Button-1>", lambda x: self.drawer.activate(self.grid_drawer))

        self.drawer.place(x=0, y=0, relheight=1.)
        self.drawer.lift()

        self.home = tk.CTkFrame(master=self.drawer, width=150, height=50)
        self.home.grid_anchor(tk.CENTER)
        self.home.grid_propagate(False)
        self.home.grid_rowconfigure(0, weight=1)
        tk.CTkLabel(master=self.home, text="", image=get_img("house.png", (27, 27))).grid(row=0, column=0)
        tk.CTkLabel(master=self.home, text="H O M E", text_color="#686868", font=(*self.master.font, "bold")).grid(
            row=0,
            column=1,
            padx=20)

        self.log = tk.CTkFrame(master=self.drawer, width=150, height=50)
        self.log.grid_anchor(tk.CENTER)
        self.log.grid_propagate(False)
        self.log.grid_rowconfigure(0, weight=1)
        tk.CTkLabel(master=self.log, text="", image=get_img("logout.png", (27, 27))).grid(row=0, column=0)
        tk.CTkLabel(master=self.log, text="L O G O U T", text_color="#686868", font=(*self.master.font, "bold")).grid(
            row=0,
            column=1,
            padx=20)


        self.drawer.grid_anchor(tk.CENTER)
        self.grid_drawer()

        self.home.bind("<Button-1>", lambda x: master.go2page("home"))
        self.log.bind("<Button-1>", lambda x: self.logout())

        self.bind("<Button-1>", lambda x: self.drawer.deactivate() if x.widget != self else None)

    def grid_drawer(self):

        self.home.grid(row=0, column=0, pady=0)
        self.home.grid_anchor(tk.CENTER)
        self.home.grid_propagate(False)
        self.home.grid_rowconfigure(0, weight=1)

        self.log.grid(row=1, column=0, pady=10)
        self.log.grid_anchor(tk.CENTER)
        self.log.grid_propagate(False)
        self.log.grid_rowconfigure(0, weight=1)


    def logout(self):
        self.master.auth.user = None
        self.master.go2page("home")



