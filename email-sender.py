import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text()) #wrapping in template to call the text with the $ variables 
email = EmailMessage()
email['from'] = 'Elizabeth'
email['to'] = 'sender@gmail.com'
email['subject'] = 'Congratulations, You just won! '

email.set_content(html.substitute({'name':'TinTin', 'amount':'$1000'}), 'html')

#for host and port, you can find this out on google for smtp
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    #initial message for the server
    smtp.ehlo()
    smtp.starttls() #encryption mechanism to connect securely 
    #connecting to gmail account 
    smtp.login('nobody@gmail.com', 'notreal!')
    smtp.send_message(email)
    print('all good!')