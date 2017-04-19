# PollenTracker
A small python script to regularly check the pollen count in an area and send notifications.

**Setup**

1. Clone Repository 
2. Add Following Enviroment variables:
```python
export GMAIL_USER = YOUR_GMAIL_EMAIL_ADDRESS
export GMAIL_PASSWORD = YOUR_GMAIL_PASSWORD
```
3. Update recipent email address list with address(s) you want the notification sent too. 
```python
notificationRecipents = [""] # ADD RECIPENT EMAILS TO THIS LIST
```
4. You can then add the application to your crontab file.

Alternatively you can run the script without sending any emails and just print the output to stdout. To do this run the file as follows: 
```python 
python main.py -o 
