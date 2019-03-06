from bs4 import BeautifulSoup
import requests
import csv
import numpy as np
import time



def getUrl(url):
    req = requests.get(url)
    return BeautifulSoup(req.content, features='html.parser')


#Generic Function will go to game site Tibia.com and scrape the highscore boards for all worlds passed in the function. The function will write a new csv file, named by the world, with all the data scraped.
def getHighScores(server):
    world = server.capitalize()
    page = 1
    total_pages = 12

    csv_file = open(f'{world}.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([f'Server: {world}'])
    csv_writer.writerow(['Rank','Name','Vocation','Level','Exp'])


    while(page <= total_pages):

        url = f'https://www.tibia.com/community/?subtopic=highscores&world=Antica&list=experience&profession=0&currentpage=1https://www.tibia.com/community/?subtopic=highscores&world={world}&list=experience&profession=0&currentpage={str(page)}'
        
        soup = getUrl(url)
        table = soup.find('table', {'class':'TableContent'})

        for tr in table.findAll('tr')[1:-1]:
            values = [td for td in tr.findAll('td')]
            rank = values[0].get_text()
            name = values[1].get_text()
            voc = values[2].get_text()
            level = values[3].get_text()
            exp = values[4].get_text()
            csv_writer.writerow([rank,name,voc,level,exp])

        page+=1
#Opening file that was created using scraper to get all "worlds" in tibia.
clean_data = []
with open('worlds.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        clean_data.append(i[0])
stripped_worlds = clean_data[1:]

#This function will take each world that was scraped from Tibia.com and run the get high score function above and write the file.
for server in stripped_worlds:
    getHighScores(server)
    time.sleep(60)

print("Whewww!")



