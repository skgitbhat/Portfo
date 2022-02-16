import smtplib
from email.message import EmailMessage
import csv
import datetime;
  

def sender(data):

  try:  
    em=data['email']
    sub=data['subject']
    mes=data['message']+f" \n \n from:   {em}"


    email = EmailMessage()
    email['from']=data['email']
    email['to'] = 'shivakumarmbhat@gmail.com'
    email['subject'] = sub

    

    email.set_content(mes)
    

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
      smtp.ehlo()
      smtp.starttls()
      smtp.login('krishnadyavru@gmail.com', 'youtubedyavru')
      smtp.send_message(email)

  except Exception as Argument:

    print(Argument)

  finally:
     with open('database.csv', newline='', mode='a') as database2:
      ct = datetime.datetime.now()
     
      
      csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([em,sub,data['message'],ct])