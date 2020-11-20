# encoding=utf8
import requests
import pandas
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


#Function which fetches the active code information from the AFK website
def getActiveCodes():
    page = requests.get('https://afk.guide/redemption-codes/')
    soup = bs(page.content, 'html.parser')
    
    table = soup.find('table')
    table = table.find('tbody')
    rows = table.find_all('tr')
    imgs = table.find_all('img')
    
    div = soup.find('div', {'data-td-block-uid':'tdi_48_566'})
    lst = div.find('ul')    # for i in lst:

    codes = []
    for li in lst.find_all('li'):
        li = li.text.encode('utf-8').decode('ascii', 'ignore')
        print(li)
        item = li.split('  ')
        codes.append((item[0].strip(), item[1].strip()))
        print('Code: {0}, Reward: {1}'.format(item[0].strip(), item[1].strip()))

    # Convert codes to a dataframe
    codedf = pandas.DataFrame(codes)
    codedf.columns = ['Codes', 'Rewards']
    
    return codedf


def sendNotif(subject, message, sender, destination):
    # Start connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # File containing login info for gmail account that will send messages
    logininfo = open('../devpass.txt')
    lines = logininfo.readlines()
    server.login(lines[0], lines[1])
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = destination
    msg.attach(MIMEText(message))
    server.sendmail(sender, destination, msg.as_string())
    server.quit()
