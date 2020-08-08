import tkinter as tk

from enum import Enum
from mail import Mailer
from screens.login import LoginScreen
from screens.mail_list import MailList
import tkinter.messagebox as tm


class Page(Enum):
    LOGIN = 1
    MAIL_LIST = 2


class Application():

    def start(self):
        self.root = tk.Tk()
        self.showPage(Page.LOGIN)

    def showPage(self, page):
        self.root.destroy()
        self.root = tk.Tk()

        if page == Page.LOGIN:
            LoginScreen(self.root, self.onLogin)
        elif page == Page.MAIL_LIST:
            MailList(self.root)

        self.root.mainloop()

    def onLogin(self, url, port, email, password):
        self.mailer = Mailer(url, port)
        login_success = self.mailer.authenticate(email, password)

        if not login_success:
            tm.showerror("Login error", "Login credentials are invalid!")
            return

        self.showPage(Page.MAIL_LIST)

    def sendMail(self, mfrom, to, subject, message):
        self.mailer.send(mfrom, to, subject, message)


if __name__ == "__main__":
    app = Application()
    app.start()
