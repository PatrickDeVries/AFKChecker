import pandas
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
    # Convert data frames to 2d lists for iteration
    newdata = np.vstack((newcodedf['Codes'].to_list(), newcodedf['Rewards'].to_list()))
    olddata = np.vstack((oldcodedf['Codes'].to_list(), oldcodedf['Rewards'].to_list()))

    # Check for new codes, ignore if one expired
    for i in range(0, len(newdata[0])):
        if newdata[0][i] not in olddata[0]:
            # Build notification message
            message = 'New Code: "' + str(newdata[0][i]) + '" for ' + str(newdata[1][i]) 
           
            # Send notification with format:
            # client.send_message("Message", "Title", "Device or Device Group ID", "Icon", "Sound", "Vibration", "URL", "URL Title", "Time2Live", "Priority", "Retry", "Expire", "Answer", "Image 1", "Image 2", "Image 3")
            Client("").send_message(message, "AFK Code Drop", "26131", "37", "0", "2", "https://afk.guide/redemption-codes/", "Go to codes", "0", "2", "60", "600", "1", "", "", "")

    newcodedf.to_csv('./AFKCodes.csv')


