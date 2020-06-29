import pandas
from Utilities import getActiveCodes, sendNotif
import numpy as np


newcodedf = getActiveCodes()
oldcodedf = pandas.read_csv('./AFKCodes.csv', index_col=0)

key = open('PrivateKey.txt')
init(key.read())

if not newcodedf.equals(oldcodedf):
    # Convert data frames to 2d lists for iteration
    newdata = np.vstack((newcodedf['Codes'].to_list(), newcodedf['Rewards'].to_list()))
    olddata = np.vstack((oldcodedf['Codes'].to_list(), oldcodedf['Rewards'].to_list()))

    # Check for new codes, ignore if one expired
    for i in range(0, len(newdata[0])):
        if newdata[0][i] not in olddata[0]:
            # Build notification message
            message = 'New Code: ' + str(newdata[0][i]) + '\nfor ' + str(newdata[1][i]) 
            message = message + '\n\nCheck codes at: https://afk.guide/redemption-codes/'
            
            # Open list of destination emails from file
            destinations = open('../emaillist.txt').readlines()     
            # Send email(s)
            for dest in destinations:
                sendNotif('AFK Code Drop', message, 'AFK Bot', dest)
                
    newcodedf.to_csv('./AFKCodes.csv')


