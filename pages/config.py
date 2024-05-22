import customtkinter as tk
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
        self.home = tk.CTkLabel(master=self, text="", image=home_icon)
        self.home.place(relx=0.0, x=10, rely=1.0,y=-30, anchor="w")
        self.log = tk.CTkLabel(master=self, text="", image=logout_icon)
        self.log.place(relx=0.0, x=10, rely=1.0,y=-75, anchor="w")
        tk.CTkEntry(master=self, textvariable=self.thrs).grid(row=1, column=0)
        tk.CTkButton(master=self, text="Küldés", command= lambda : master.send_command(self.thrs.get())).grid(row=2, column=0)

        self.home.bind("<Button-1>", lambda x: master.go2page("home"))
        self.log.bind("<Button-1>", lambda x: self.logout())



    def update(self):
        self.after(100, self.update)


    def mainloop(self, n = 0):
        self.update()
        super().mainloop(n)

    def logout(self):
        self.master.auth.user = None
        self.master.go2page("home")