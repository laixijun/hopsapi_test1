# coding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# ----------邮件相关参数------
smtpserver = "smtp.qq.com"           # 发件服务器
port = 465                              # 端口
sender = "295841794@qq.com"     # 账号
psw = "vtaopysgciypbhhe"                  # 密码
# receiver = ["xxxx@qq.com"]      # 单个接收人也可以是list
receiver = ['1020034565@qq.com', 'cqyyrs@hotmail.com', '295841794@qq.com']   # 多个收件人list对象


# ----------发送邮件------
def sendmail():
    # ----------编辑邮件的内容------
    report_dir = './report/'
    lists = os.listdir(report_dir)
    # lists.sort(key=lambda filename: os.path.getctime(report_dir+filename))
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + fn))
    report_file_path = os.path.join(report_dir, lists[-1])

    with open(report_file_path, "rb") as fp:
        mail_body = fp.read()
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = ";".join(receiver)  # 多个收件人list转str
    msg["subject"] = "cms_api-测试报告"  # 主题
    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    # att = MIMEText(mail_body, "base64", "utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    att = MIMEApplication(open(report_file_path, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(report_file_path))
    msg.attach(att)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)                      # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)                       # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()                                       # 关闭连接