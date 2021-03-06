import pandas as pd
from Utilities import getActiveCodes, sendNotif
import numpy as np


newcodedf = getActiveCodes()
oldcodedf = pd.read_csv('./AFKCodes.csv', index_col=0)

if not newcodedf.equals(oldcodedf):
    # Convert data frames to 2d lists for iteration
    newdata = np.vstack((newcodedf['Codes'].values, newcodedf['Rewards'].values))
    olddata = np.vstack((oldcodedf['Codes'].values, oldcodedf['Rewards'].values))

    # Check for new codes, ignore if one expired
    for i in range(0, len(newdata[0])):
        if newdata[0][i] not in olddata[0]:
            # Build notification message
            message = 'New Code: ' + str(newdata[0][i]) + '\nfor ' + str(newdata[1][i]) 
            message = message + '\n\nCheck codes at: https://afk.guide/redemption-codes/'
            d = {'Codes': [str(newdata[0][i])], 'Rewards': [str(newdata[1][i])]}
            newVal = pd.DataFrame(data=d)
            oldcodedf = pd.concat([oldcodedf, newVal], ignore_index=True)
            # Open list of destination emails from file
            destinations = open('../emaillist.txt').readlines()     
            # Send email(s)
            for dest in destinations:
                sendNotif('AFK Code Drop', message, 'AFK Bot', dest)

# print(oldcodedf)
oldcodedf.to_csv('./AFKCodes.csv')


