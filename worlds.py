from bs4 import BeautifulSoup
import requests
import csv



def getUrl(url):

    req = requests.get(url)

    return BeautifulSoup(req.content, features='html.parser')

csv_file = open('worlds.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tibia Servers:'])

soup = getUrl('https://www.tibia.com/community/?subtopic=worlds')

# div = soup.find('div', {'class':'TableContentAndRightShadow'}).find('div', {'class':'TableContentContainer'}).find('table', {'class':'TableContent'}).findAll('tr')
tr = soup.findAll('tr', {'class':['Odd','Even']})

for row in tr:
    value = [td for td in row]
    server = value[0].get_text()
    csv_writer.writerow([server])

