import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from threading import Timer
import datetime
import time
import psutil
import sys
import os

class ev:
        def __init__(self):
            self.smtpHost = ""
            self.port = 0
            self.sendAddr = ""
            self.password = ""
            self.recipientAddrs = ""
            self.subject = ""
            self.content = ""
            self.txtpath = ""
            self.readpath = ""
            self.delaysendtime = 3600
#修改以下参数
ev.smtoHost = "smtp.163.com"             #邮箱STMP服务器地址
ev.port = 465                            #发送端口
ev.sendAddr = "xxxxxxx@163.com"      #发送邮箱
ev.password = "xxxxxxxxxxx"         #STMP授权码
ev.recipientAddrs = "xxxxxxx@qq.com"  #收件方可以是多个邮箱,用";"分开
ev.subject = "电脑开启"              #邮件标题
ev.content = "数据收集中"                #邮件内容（默认后面跟时间）

ev.txtpath = "C:\\Users\\1\\Documents\\save.txt"  #需要自行创建 例：C:\\Users\\OthersUser\\Documents\\save.txt
ev.readpath = "C:\\Users\\1\\Documents\\save.txt"
ev.delaysendtime = 3600                           #可不设置，默认3600秒发送一次（第一次开机发送 第二次5分钟发送，第三次开始按照该时间发送）

#特定监控相关进程（需要更多请继续添加，目前开放一个，后续优化设计）
thread1 = "Code.exe"#监控的后台进程文件访问位置，填入进程名，例：Code.exe



#邮件发送相关

def send_email_redo(smtpHost = ev.smtoHost,port = ev.port, sendAddr = ev.sendAddr, password = ev.password, recipientAddrs = ev.recipientAddrs, subject=ev.subject):
    date = datetime.date.today()
    date2 = datetime.datetime.now()
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = ev.content + str(date2)
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)
    print("准备添加附件...")
    
    part = MIMEApplication(open(ev.txtpath,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="data.txt")
    msg.attach(part)
    smtp = smtplib.SMTP_SSL(smtpHost, port)
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs.split(";"), str(msg))
    print("发送成功！")
#电脑参数相关
def computer_now_status():
    date = datetime.date.today()
    date2 = datetime.datetime.now()
    try:
        fw = open(ev.readpath, 'w') 
        for proc in psutil.process_iter(['pid', 'name']):
            print(proc.info)
            i = str(proc.info)
            fw.write(str(proc.info)+"\n")
            fw.write(str(date2)+"\n")
            if proc.info['name'] == 'explorer.exe':
                pidnow = proc.info['pid']
                print(pidnow)
                p = psutil.Process(pidnow)
                print(p.exe())
                #print(p.open_files())
                fw.write(str(p.cwd()) + "\n" + str(p.exe()) + "\n")
                print(p.cwd())
            if proc.info['name'] == 'UV4.exe':
                pidnow = proc.info['pid']
                print(pidnow)
                p = psutil.Process(pidnow)
                print(p.exe())
                fw.write(str(p.cwd()) + "\n" + str(p.exe()) + "\n")
                print(p.cwd())
            if proc.info['name'] == thread1:
                pidnow = proc.info['pid']
                print(pidnow)
                p = psutil.Process(pidnow)
                print(p.exe())
                fw.write(str(p.cwd()) + "\n" + str(p.exe()) + "\n")
                print(p.cwd())
                
                
        time.sleep(5)
        
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    i = 0
    while(True):
        i += 1
        try:
            if(i == 1):
                computer_now_status()
                send_email_redo()
            if(i == 2):
                time.sleep(300)#5分钟
                computer_now_status()
                send_email_redo()
            else:
                time.sleep(ev.delaysendtime)#自定义分钟
                computer_now_status()
                send_email_redo()
        except Exception as err:
            print(err)
