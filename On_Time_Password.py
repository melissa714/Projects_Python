
import random 
import smtplib
from email.message import EmailMessage




for i in range(6):
    var=random.randrange(0,10) 
    print(var)


message = EmailMessage()
message['Subject']="bonjour"
message['From']='kanangemelissanguessan@gmail.com'
message['To']='nguessanmelissa01@gmail.com'

message.set_content('c est un test')

