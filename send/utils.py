from django.conf import settings
from django.core.mail import EmailMessage


def send_custom_email(subject, message, recipients):
    try:
        email_message = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Sender's email
            [recipients]  # Receiver's email

        )
        email_message.send(fail_silently=False)
        print('email sent')
    except Exception as e:
        print(str(e))