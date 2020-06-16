# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# ----------1.跟发件相关的参数------
smtpserver = "smtp.qq.com"           # 发件服务器
port = 465                              # 端口
sender = "295841794@qq.com"     # 账号
psw = "vtaopysgciypbhhe"                  # 密码
# receiver = ["xxxx@qq.com"]      # 单个接收人也可以是list
receiver = ['1020034565@qq.com', 'cqyyrs@hotmail.com', '295841794@qq.com']   # 多个收件人list对象


# ----------2.编辑邮件的内容------
# 读文件
report_path = "./report/result.html"
with open(report_path, "rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender                       # 发件人
msg["to"] = ";".join(receiver)             # 多个收件人list转str
msg["subject"] = "cms_api-测试报告"              # 主题
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)

# 附件
#att = MIMEText(mail_body, "base64", "utf-8")
#att["Content-Type"] = "application/octet-stream"
#att["Content-Disposition"] = 'attachment; filename="test_report.html"'
att = MIMEApplication(open(report_path, 'rb').read())
att.add_header('Content-Disposition', 'attachment', filename='test_report.html')
msg.attach(att)


# ----------3.发送邮件------
def sendmail():
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)                      # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)                       # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()                                       # 关闭