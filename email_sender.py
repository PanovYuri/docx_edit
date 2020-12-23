from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import encoders
import os
import smtplib

# filepath = os.path.join(os.getcwd(), 'pdf', '12.12 Приморский край АО 30 СУДОРЕМОНТНЫЙ ЗАВОД.pdf')
# basename = os.path.basename(filepath)
address = 'k.nuriahmetowa@yandex.ru'

# # Create Message
# part = MIMEBase('application', "octet-stream")
# part.set_payload(open(filepath,"rb").read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)

# # Compose message
# msg = MIMEMultipart()
# msg['From'] = 'u.panow@yandex.ru'
# msg['To'] = address
# msg.attach(part)

# Send email
smtp = smtplib.SMTP('smtp.yandex.ru', 465)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login('u.panow@yandex.ru', 'zont2001!')
smtp.sendmail('u.panow@yandex.ru', address, "Hello")
smtp.quit()