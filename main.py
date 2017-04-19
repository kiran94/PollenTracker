#!/usr/bin/python

import os
import sys
from services.BBCPollenService import BBCPollenService
from services.EmailService import EmailService

gmailUser = os.environ.get("GMAIL_USER")
gmailPassword = os.environ.get("GMAIL_PASSWORD")
notificationRecipents = [""] # ADD RECIPENT EMAILS TO THIS LIST

sendEmail = True
if len(sys.argv) > 0 and (sys.argv[0] == "--output" or "-o"):
	sendEmail = False

pollenService = BBCPollenService()
emailService = EmailService(gmailUser, gmailPassword)

pollen = pollenService.getPollenFlag()
print pollen

if (sendEmail and (pollen == "Very High" or pollen == "High" or pollen == "Low")):
	result = emailService.sendEmail(
		notificationRecipents, 
		gmailUser, 
		"Pollen Count", 
		"The pollen count for today was found to be {}. Make sure you take any medication.".format(pollen))

	if (result):
    		print "Email sent successfully."
	else:
    		print "Email failed."


print "Done."