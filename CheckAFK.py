import requests
import pandas
from bs4 import BeautifulSoup as bs
from pushsafer import init, Client

page = requests.get('https://afk.guide/redemption-codes/')
# print(page)

soup = bs(page.content, 'html.parser')
items = soup.find_all('code')
newcodes = [x.get_text() for x in items]

newcodedf = pandas.DataFrame(newcodes)
newcodedf.columns = ['Codes']

oldcodedf = pandas.read_csv('./AFKCodes.csv', index_col=0)

# init("PrivateKey")
# Client("").send_message("Message", "Hello", "26131", "10", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "60", "600", "1", "", "", "")
key = open('PrivateKey.txt')
init(key.read())
if newcodedf.equals(oldcodedf):
    Client("").send_message('No new codes today', "AFK Code drop", "26131", "37", "0", "2", "https://afk.guide/redemption-codes/", "Go to codes", "0", "2", "60", "600", "1", "", "", "")

else:
    newcodelist = newcodedf['Codes'].to_list()
    oldcodelist = oldcodedf['Codes'].to_list()
    # oldser = pd.series(oldcodedf)
    # Check for new codes
    for i in newcodelist:
        # print(i)
        if i not in oldcodelist:
            # sent notif
            message = 'New Code: ' + str(i) 
            
            # client.send_message("Message", "Title", "Device or Device Group ID", "Icon", "Sound", "Vibration", "URL", "URL Title", "Time2Live", "Priority", "Retry", "Expire", "Answer", "Image 1", "Image 2", "Image 3")

            Client("").send_message(message, "AFK Code Drop", "26131", "37", "0", "2", "https://afk.guide/redemption-codes/", "Go to codes", "0", "2", "60", "600", "1", "", "", "")

    newcodedf.to_csv('./AFKCodes.csv')


