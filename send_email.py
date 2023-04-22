import smtplib
import ssl
import os

# Define a function to send an email with a given message
def send_email(message):
    # Set the SMTP server information
    host = "smtp.gmail.com"   # The hostname or IP address of the SMTP server that you want to connect to.
    port = 465   # The port number to use for the SMTP server. For SMTP_SSL, the default port is 465.

    # Set the email credentials for the sender
    user_name = "MyPythonPortfolio@gmail.com"   # The email username - used to connect to the email account that will send the message
    password = os.getenv("PASSWORD")   # The app password - used to authenticate the email account that will send the message

    # Set the email address of the receiver
    receiver = "MyPythonPortfolio@gmail.com"   # The email address of the receiver

    # Create a secure SSL context
    context = ssl.create_default_context()   # A context is a set of parameters or options that define the security and communication settings for a particular operation or protocol.

    # Connect to the SMTP server using SSL and send the email message
    with smtplib.SMTP_SSL(host, port, context=context) as server:   # We use "context" as a key parameter because the order of the parameters matters. We could also pass in "context=context" to be more explicit.
        server.login(user_name, password)   # Log in to the email account that will send the message
        server.sendmail(user_name, receiver, message)   # Send the email message to the receiver
