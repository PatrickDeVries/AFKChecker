import requests
import pandas
from bs4 import BeautifulSoup as bs

# page = requests.get('https://afk.guide/redemption-codes/')

# print(page)

# soup = bs(page.content, 'html.parser')
# # print(soup)

# items = soup.find_all('code')
# print(items)

# codes = [x.get_text() for x in items]

# print(codes)

# codedf = pandas.DataFrame(codes)
# codedf.columns = ['Codes']
# print(codedf)


# items = soup.find_all('td', style='width: 33.046%;'or'width: 33.046%; height: 26px;')
# items2 = soup.find_all('td', style='width: 33.046%; height: 26px;')

# print(items)
# print(items2)
# rewards = [x.get_text() for x in items]
# for i in items2:
#     rewards.append(i.get_text())
# print(rewards)

def getActiveCodes():
    page = requests.get('https://afk.guide/redemption-codes/')
    soup = bs(page.content, 'html.parser')
    
    table = soup.find('table')
    table = table.find('tbody')
    rows = table.find_all('tr')
    imgs = table.find_all('img')

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

        #Join rewards list into one string
        row[-1] = ', '.join(row[-1])
        
        codes.append(row)
        
    codedf = pandas.DataFrame(codes)
    codedf.columns = ['Codes', 'Rewards']
    return codedf


df = getActiveCodes()
df.to_csv('./AFKCodes.csv')

    # oldcodedf = pandas.read_csv('./AFKCodes.csv', index_col=0)
