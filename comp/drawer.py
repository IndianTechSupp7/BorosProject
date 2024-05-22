import customtkinter as tk


class Drawer(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master = master, height=500, width = 0)
        self.grid_propagate(False)
        self.animation = 0
        self.expand_width = 200
        self.grd_func = lambda : ...

    def grid_forget_children(self):
        for child in self.winfo_children():  # Get all the children of the parent widget
            child.grid_forget()
        print(self.winfo_children())



    def activate(self, grid):
        if self.animation == 0:
            grid()
        self.animation = min(self.animation + 0.05, 1)
        self.configure(width=self.expand_width * self.animation)
        if self.animation < 1:
            self.after(1, lambda : self.activate(grid))



    def deactivate(self):
        self.grid_forget_children()
        self.animation = max(self.animation - 0.05, 0)
        self.configure(width=self.expand_width * self.animation)
        if self.animation > 0:
            self.after(1, self.deactivate)



    @staticmethod
    def lerp(a, b, t):
        return a + (b - a) * t


    def update(self):
        self.after(1, self.update)
    
    
    def mainloop(self, n = 0):
        self.update()
        super().mainloop(n)
