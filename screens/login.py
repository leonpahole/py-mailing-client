import tkinter as tk
import tkinter.messagebox as tm


class LoginScreen(tk.Frame):
    def __init__(self, master, onLogin):
        super().__init__(master)

        self.label_server_url = tk.Label(self, text="Server url")
        self.label_port = tk.Label(self, text="Port")
        self.label_email = tk.Label(self, text="Username")
        self.label_password = tk.Label(self, text="Password")

        self.entry_server_url = tk.Entry(self)
        self.entry_port = tk.Entry(self)
        self.entry_email = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.label_server_url.grid(row=0, sticky=tk.E)
        self.label_port.grid(row=1, sticky=tk.E)
        self.label_email.grid(row=2, sticky=tk.E)
        self.label_password.grid(row=3, sticky=tk.E)

        self.entry_server_url.grid(row=0, column=1)
        self.entry_port.grid(row=1, column=1)
        self.entry_email.grid(row=2, column=1)
        self.entry_password.grid(row=3, column=1)

        self.logbtn = tk.Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.entry_server_url.insert(0, 'smtp.gmail.com')
        self.entry_port.insert(0, '465')
        self.entry_email.insert(0, 'leon.pahole@gmail.com')
        self.entry_password.insert(0, '2bfFmpoJsXJ90wZe4zUb0uvw0mHn34')

        self.onLogin = onLogin

        self.pack()

    def _login_btn_clicked(self):
        url = self.entry_server_url.get().strip()
        port = self.entry_port.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        if len(url) == 0:
            tm.showerror("Input error", "Please enter server url!")
        elif len(port) == 0:
            tm.showerror("Input error", "Please enter server port!")
        elif not port.isnumeric():
            tm.showerror("Input error", "Please enter valid port number!")
        elif len(email) == 0:
            tm.showerror("Input error", "Please enter email!")
        elif len(password) == 0:
            tm.showerror("Input error", "Please enter password!")
        else:
            self.onLogin(url, port, email, password)
