import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = argv[1]
password = argv[2]
print(argv)
print(argv[1])
print(argv[2])
to_addr = ['v-xisu@microsoft.com', 'xiuxi.sun@qq.com']
    
smtp_server = 'smtp.qq.com'
 
msg = MIMEText('DEV ver pipeline test fail，detail info as Link：*******','plain','utf-8')
     
msg['From'] = Header(from_addr)
msg['Subject'] = Header('ansible-collection DEV TEST')
    
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
server.login(from_addr, password)
for mail_box in to_addr:
    msg['To'] = Header(mail_box)
    server.sendmail(from_addr, mail_box, msg.as_string())
server.quit()
