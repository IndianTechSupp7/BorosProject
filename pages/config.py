import customtkinter as tk

from comp.core_func import get_img
from comp.drawer import Drawer
from comp.page import Page
from PIL import Image

class ConfigPage(Page):
    def __init__(self, master):
        super().__init__(master = master)
        self.grid_anchor(tk.CENTER)

        self.thrs = tk.StringVar(value="20")

        home_icon = tk.CTkImage(light_image=Image.open('assets/house.png'),
                                          dark_image=Image.open('assets/house.png'),
                                          size=(27, 27))
        logout_icon = tk.CTkImage(light_image=Image.open('assets/logout.png'),
                                dark_image=Image.open('assets/logout.png'),
                                size=(27, 27))

        tk.CTkLabel(master=self, text="ConfigPage").grid(row=0, column=0)
        self.drawer = Drawer(master=self)

        self.menu = tk.CTkLabel(master=self, text="", image=get_img("more.png", (27, 27)))
        self.menu.place(x=10, y=10)
        self.menu.bind("<Button-1>", lambda x: self.drawer.activate(self.grid_drawer))

        # self.home = tk.CTkLabel(master=self, text="", image=home_icon)
        # self.home.place(relx=0.0, x=10, rely=1.0,y=-30, anchor="w")
        # self.log = tk.CTkLabel(master=self, text="", image=logout_icon)
        # self.log.place(relx=0.0, x=10, rely=1.0,y=-75, anchor="w")
        tk.CTkEntry(master=self, textvariable=self.thrs).grid(row=1, column=0)
        tk.CTkButton(master=self, text="Küldés", command= lambda : master.send_command(self.thrs.get())).grid(row=2, column=0)

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


    def update(self):
        self.after(100, self.update)


    def mainloop(self, n = 0):
        self.update()
        super().mainloop(n)

    def logout(self):
        self.master.auth.user = None
        self.master.go2page("home")