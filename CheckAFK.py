import requests
import pandas
from bs4 import BeautifulSoup as bs
from pushsafer import init, Client
from Utilities import getActiveCodes
import numpy as np


newcodedf = getActiveCodes()
oldcodedf = pandas.read_csv('./AFKCodes.csv', index_col=0)

# init("PrivateKey")
# Client("").send_message("Message", "Hello", "26131", "10", "0", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "60", "600", "1", "", "", "")

key = open('PrivateKey.txt')
init(key.read())

if newcodedf.equals(oldcodedf):
    Client("").send_message('No new codes today', "AFK Code drop", "26131", "37", "0", "2", "https://afk.guide/redemption-codes/", "Go to codes", "0", "2", "60", "600", "1", "", "", "")
else:
    newcodelist = newcodedf['Codes'].to_list()
    newrewardlist = newcodedf['Rewards'].to_list()
    oldcodelist = oldcodedf['Codes'].to_list()
    oldrewardlist = oldcodedf['Rewards'].to_list()
    newdata = np.vstack((newcodelist, newrewardlist))
    olddata = np.vstack((oldcodelist, oldrewardlist))

    # Check for new codes, ignore if one expired
    for i in range(0, len(newdata[0])):
        print(newdata[0][i], newdata[1][i])
        if newdata[0][i] not in olddata[0]:
            # sent notif
            message = 'New Code: "' + str(newdata[0][i]) + '" for ' + str(newdata[1][i]) 
            
            # client.send_message("Message", "Title", "Device or Device Group ID", "Icon", "Sound", "Vibration", "URL", "URL Title", "Time2Live", "Priority", "Retry", "Expire", "Answer", "Image 1", "Image 2", "Image 3")
            Client("").send_message(message, "AFK Code Drop", "26131", "37", "0", "2", "https://afk.guide/redemption-codes/", "Go to codes", "0", "2", "60", "600", "1", "", "", "")

    newcodedf.to_csv('./AFKCodes.csv')


