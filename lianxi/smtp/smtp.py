#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  #设置服务器
mail_user = "444360441@qq.com"  #用户名
mail_pass = "rtlsaramxvojbieh"  #口令

sender = '444360441@qq.com'
receivers = ['17610551318@163.com', '69363233@qq.com']



def sendEmail(email):
    message = MIMEText('Python 邮件发送测试。。。', 'plain', 'utf-8')
    message['From'] = Header('福昕互联', 'utf-8')
    message['To'] = Header(email, 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        print(1)
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        print('邮件正在发送')
        smtpObj.sendmail(sender, email, message.as_string())
        smtpObj.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('发送失败')


for email in receivers:
    sendEmail(email)