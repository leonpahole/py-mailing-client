import tkinter as tk


class MailList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = tk.Label(self, text="Test")
        self.label_password = tk.Label(self, text="TEST")

        self.label_username.grid(row=0, sticky=tk.E)
        self.label_password.grid(row=1, sticky=tk.E)

        self.pack()
