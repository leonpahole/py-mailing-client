import smtplib
# from email import encoders
from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class Mailer:

    def __init__(self, url, port):
        self.server = smtplib.SMTP_SSL(url, port)
        self.server.ehlo()

    def authenticate(self, email, password):
        try:
            self.server.login(email, password)
            return True
        except smtplib.SMTPAuthenticationError:
            return False

    def send(self, mfrom, to, subject, message):
        msg = MIMEMultipart()
        msg['From'] = mfrom
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        text = msg.as_string()
        self.server.sendmail(mfrom, to, text)


"""
filename = 'test.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)
"""
