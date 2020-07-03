import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

sender_email = "sender@sender.com"
receiver_email = ['receiver@receiver.com']

message = MIMEMultipart("alternative")
message["Subject"] = "Email me"
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

text = """
Hi,

Email received!:


"""
dicts = {}

#message = MIMEMultipart("alternative", None, [MIMEText(text), MIMEText(html,'html')])


part1 = MIMEText(text, "plain")
# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)

#Change the smtp details if needed
server = smtplib.SMTP("smtp.office365.com",587)
server.ehlo()
server.starttls()
server.ehlo
# Create secure connection with server and send email
server.login("sender@sender.com", "sender@321")
server.sendmail(sender_email, receiver_email, message.as_string())
