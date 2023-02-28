import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = 'stephentian@foxmail.com'
receivers = ['745752067@qq.com']
mail_host = 'smtp.qq.com'

mail_msg = """
<p>商城脚本 邮件发送测试...</p>
<p><a href="https://www.louisvuitton.cn/zhs-cn/products/boite-chapeau-souple-mm-monogram-nvprod2440099v/M45647">快速进入商品链接</a></p>
"""


message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('测试', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = '商城购物邮件通知'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    # smtpObj = smtplib.SMTP_SSL(mail_host1, port=465)
    smtpObj.set_debuglevel(1)
    smtpObj.connect(mail_host)
    # smtpObj.connect(mail_host1, port=465)
    smtpObj.login(sender, "")
    smtpObj.sendmail(sender, receivers, message.as_string())

    print('邮件发送成功')
    smtpObj.quit()
except smtplib.SMTPException as e:
# except Exception as e:
		print("Error: ", str(e))
