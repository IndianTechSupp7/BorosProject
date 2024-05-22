import customtkinter as ctk

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("300x200")

    # Create a frame containing widgets
    frame = ctk.CTkFrame(root, bg_color="#FFFFFF")
    frame.pack(fill="both", expand=True)

    # Create buttons inside the frame
    button1 = ctk.CTkButton(frame, text="Button 1")
    button1.grid(row=0, column=0)

    button2 = ctk.CTkButton(frame, text="Button 2")
    button2.grid(row=0, column=1)

    # Disable resizing of the frame
    root.grid_rowconfigure(0, weight=1)  # Allow the frame to expand vertically
    root.grid_columnconfigure(0, weight=1)  # Allow the frame to expand horizontally

    root.mainloop()
