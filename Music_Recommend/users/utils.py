from django.core.mail import EmailMessage

from smtplib import SMTPException
import logging
import threading


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.email.send()
            
        except Exception as e:
            raise e 

class EmailUtil:

    @staticmethod
    def send_async_email(message):
        email = EmailMessage(
            subject=message["email_subject"],
            body=message["email_body"],
            to=[message["to_email"]],
        )
        try:
            EmailThread(email).start()
        
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            raise e