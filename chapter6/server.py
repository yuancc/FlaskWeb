'''
关于flask中的电子邮件
用qqmail做实验
由于gmail不知道为什么不能开启应用密码功能
'''
# vxerwvngorqugaei

from flask import Flask
import os
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# 获取环境变量中的账号和密码
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False


mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/')
def index():
    print(os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASSWORD'))
    msg = Message(subject="我是葛松", sender=os.environ.get('MAIL_USERNAME'),
                  recipients=[os.environ.get('MAIL_USERNAME')])
    msg.body = 'testing'
    msg.html = '<b>Flask Chapter6</b>'
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run(debug=True)
