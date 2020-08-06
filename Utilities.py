import requests
import pandas
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Function which fetches the active code information from the AFK website
def getActiveCodes():
    page = requests.get('https://afk.guide/redemption-codes/')
    soup = bs(page.content, 'html.parser')
    
    table = soup.find('table')
    table = table.find('tbody')
    rows = table.find_all('tr')
    imgs = table.find_all('img')

    #Get list of alt texts for images
    alts = [img['alt'] for img in table.find_all('img', alt=True)]
    altused = 0
    codes = []

    for tr in rows:
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        # Remove extra text from codes and turn rewards into a list split by spaces
        row = [row[0].split(" ")[0], row[-1].replace(u'\xa0', u' ').split(' ')]
        
        # Add image alts
        for i in range(0, len(row[-1])):
            alt = alts[altused]
            altused+=1
            row[-1][i] = row[-1][i] + ' ' + alt

        # Join rewards list into one string
        row[-1] = ', '.join(row[-1])
        
        codes.append(row)
    
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
    print(msg.as_string())
    server.sendmail(sender, destination, msg.as_string())
    server.quit()
