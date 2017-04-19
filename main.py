#!/usr/bin/python

import os
from services.BBCPollenService import BBCPollenService
from services.EmailService import EmailService

gmailUser = os.environ.get("GMAIL_USER")
gmailPassword = os.environ.get("GMAIL_PASSWORD")
notificationRecipents = [""] # ADD RECIPENT EMAILS TO THIS LIST

pollenService = BBCPollenService()
emailService = EmailService(gmailUser, gmailPassword)

pollen = pollenService.getPollenFlag()
print pollen

if (pollen == "Very High" or pollen == "High" or pollen == "Low"):
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