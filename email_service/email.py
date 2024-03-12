from abc import ABC, abstractmethod
from typing import Dict


class MailSender(ABC):
    @abstractmethod
    def send_mail(self, to: str, subject: str, body: str) -> bool:
        pass


class TwilioMailSender(MailSender):
    def __init__(self, twilio_config: Dict[str, str]):
        self.twilio_config = twilio_config

    def send_mail(self, to: str, subject: str, body: str) -> bool:
        # Implement Twilio mail sending logic using twilio_config
        print(f"Sending Twilio mail to: {to}\nSubject: {subject}\nBody: {body}")
        return True


class MailchimpMailSender(MailSender):
    def __init__(self, mailchimp_config: Dict[str, str]):
        self.mailchimp_config = mailchimp_config

    def send_mail(self, to: str, subject: str, body: str) -> bool:
        # Implement Mailchimp mail sending logic using mailchimp_config
        print(f"Sending Mailchimp mail to: {to}\nSubject: {subject}\nBody: {body}")
        return True


class SmtpMailSender(MailSender):
    def __init__(self, smtp_config: Dict[str, str]):
        self.smtp_config = smtp_config

    def send_mail(self, to: str, subject: str, body: str) -> bool:
        # Implement SMTP mail sending logic using smtp_config
        print(f"Sending SMTP mail to: {to}\nSubject: {subject}\nBody: {body}")
        return True

# app = FastAPI()
#
# # Configuration settings
# MAIL_SENDER_PROVIDER = "smtp"  # Set to "twilio" or "mailchimp" to use respective mail sender provider
# TWILIO_CONFIG = {
#     "account_sid": "your_twilio_account_sid",
#     "auth_token": "your_twilio_auth_token",
#     # Add more Twilio configuration as needed
# }
# MAILCHIMP_CONFIG = {
#     "api_key": "your_mailchimp_api_key",
#     # Add more Mailchimp configuration as needed
# }
# SMTP_CONFIG = {
#     "host": "smtp.example.com",
#     "port": "587",
#     "username": "username",
#     "password": "password",
#     # Add more SMTP configuration as needed
# }

# Create mail sender instance based on configuration
# if MAIL_SENDER_PROVIDER == "twilio":
#     mail_sender = TwilioMailSender(TWILIO_CONFIG)
# elif MAIL_SENDER_PROVIDER == "mailchimp":
#     mail_sender = MailchimpMailSender(MAILCHIMP_CONFIG)
# elif MAIL_SENDER_PROVIDER == "smtp":
#     mail_sender = SmtpMailSender(SMTP_CONFIG)
# else:
#     raise ValueError("Invalid mail sender provider specified in configuration")
#
# @app.get("/")
# async def send_mail():
#     # Call send_mail method based on selected mail sender provider
#     mail_sender.send_mail("recipient@example.com", "Test Subject", "Test Body")
#     return {"message": "Mail sent successfully"}
