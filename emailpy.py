import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = '<Enter mail id>'
PASSWORD = '<Enter Password>'

def send_email(name,user_domain,zomato_response):
  # set up the SMTP server
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  s.login(MY_ADDRESS, PASSWORD)

  # For each contact, send the email:
  # for name, email in zip(names, emails):
  msg = MIMEMultipart()       # create a message

  # add in the actual person name to the message template
  message = "Hello, "+name+"\n"+zomato_response

  # Prints out the message body for our sake
  print(message)

  # setup the parameters of the message
  msg['From']=MY_ADDRESS
  msg['To']=user_domain
  msg['Subject']="Foodie"
  
  # add in the message body
  msg.attach(MIMEText(message, 'plain'))
  
  # send the message via the server set up earlier.
  s.send_message(msg)
  del msg
      
  # Terminate the SMTP session and close the connection
  s.quit()