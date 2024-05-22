
import customtkinter as tk
from comp.page import Page
from comp.auth import Auth


class LoginPage(Page):
    def __init__(self, master):
        super().__init__(master = master)
        self.grid_anchor(tk.CENTER)


        self.username_entry = tk.CTkEntry(master=self, placeholder_text="Felhasználónév", font=master.font)
        self.username_entry.grid(row=0, column=0, pady=10)
        self.password_entry = tk.CTkEntry(master=self, placeholder_text="Jelszó", show="*",  font=master.font)
        self.password_entry.grid(row=1, column=0, pady=10)
        tk.CTkButton(master=self, text="Belépés", font=master.font, command=self.validate).grid(row=2, column=0, pady=10)
        lnk = tk.CTkLabel(master=self, text="vissza", text_color="#1f6aa5", cursor="hand2", font=(*master.font, "underline"))
        lnk.grid(row=3, column=0, pady=5)
        lnk.bind("<Button-1>", lambda x: master.go2page("home"))

        self.debug_lable = tk.CTkLabel(master=self, text="", font=(master.font[0], 12))
        self.debug_lable.grid(row=4, column=0, pady=10)


    def validate(self):
        valid = self.master.auth.validate(self.username_entry.get(), self.password_entry.get())
        if valid:
            self.master.go2page("config")
            return
        self.debug_lable.configure(text="Rossz felhasználónév vagy jelszó!")





