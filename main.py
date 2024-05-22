import customtkinter as tk
import serial
import time

from comp.auth import Auth
from pages.home import HomePage
from pages.login import LoginPage
from comp.page import Page
from pages.config import ConfigPage

import threading


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x500")
        self.grid_anchor(tk.CENTER)
        self.font = ("Helvetica", 14)
        self.auth = Auth()

        self.hm = tk.StringVar(value="20")



        # oldalak kezelése
        Page.current = "home" # kezdő oldal
        self.tmp_page = Page.current
        self.pages = {
            "home" : HomePage(self),
            "login" : LoginPage(self),
            "config" : ConfigPage(self),
        }
        self.pages[Page.current].pack(fill='both', expand=True)

        arduino_port = 'COM3'  # For Windows
        # arduino_port = '/dev/ttyUSB0'  # For Linux
        baud_rate = 9600
        timeout = 1  # In seconds

        self.ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
        time.sleep(2)
        self.cursor = True



    @staticmethod
    def go2page(page):
        Page.current = page



    def send_command(self, command):
        self.ser.write(f"{command}".encode())

    def handle_arduino(self):
        try:
            while True:
                if self.ser.in_waiting > 0:
                    line = self.ser.readline().decode('utf-8').rstrip()
                    print(f"Received data: {line}")
                    self.hm.set(str(round(float(line), 1)))

        except KeyboardInterrupt:
            print("Exiting...")




    def update(self):
        # oldalak kezelése
        if Page.current != self.tmp_page:
            self.pages[Page.current].pack(fill='both', expand=True)
            self.pages[self.tmp_page].pack_forget()
            self.tmp_page = Page.current


        self.after(100, self.update)

    
    def mainloop(self, n = 0):
        threading.Thread(target=self.handle_arduino).start()
        self.update()
        super().mainloop(n)



if __name__ == '__main__':
    App().mainloop()


