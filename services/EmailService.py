import smtplib
import os 

# Class for sending emails. 
class EmailService:
    
    # Gmail User field. 
    user = None

    # Gmail password field. 
    password = None

    # Initialises a new instance of the email service with the user and password details. 
    def __init__(self, user, password):
        self.user = user
        self.password = password

    # Sends an email to the passed mail list, from the sender with the subject + body. 
    # Returns True if sending mail was successful, else False. 
    def sendEmail(self, to, sender, subject, body):
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (sender, ", ".join(to), subject, body)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()

            server.login(self.user, self.password)
            server.sendmail(sender, to, message)

            server.close()
            return True
        except SMTPException:            
            return False