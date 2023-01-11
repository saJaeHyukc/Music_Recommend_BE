from django.core.mail import EmailMessage

class Util:

    @staticmethod
    def send_email(message):
        email = EmailMessage(subject=message["email_subject"], body=message["email_body"], to=[message["to_email"]])
        email.send()