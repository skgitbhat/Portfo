import smtplib
from email.message import EmailMessage

def sender(mail,sub,mes):
  email = EmailMessage()
  email['from'] = mail
  email['to'] = 'shivakumarmbhat@gmail.com'
  email['subject'] = sub

  email.set_content(mes)
  

  with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('krishnadyavru@gmail.com', 'youtubedyavru')
    smtp.send_message(email)
    