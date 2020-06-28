from Utilities import getActiveCodes

df = getActiveCodes()
df.to_csv('./AFKCodes.csv')