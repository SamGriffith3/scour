import requests
from bs4 import BeautifulSoup
import _csv as csv


def search():
    #city = input("Your Town/City: ")   Put this in later to replace "town" variable
    town = "greenville"
    craigslist = 'http://' + town + ".craigslist.org/search/zip"
    print(craigslist)
    r = requests.get(craigslist).text
    first_file = "C:\\Users\\Sam\\Documents\\first.csv"
    soup = BeautifulSoup(r, 'html.parser')
    name_box = soup.find('a', attrs={'class': 'result-title hdrlnk'})
    time_box = soup.find('time', attrs={'class': 'result-date'})
    name = name_box.text
    time = time_box.text

    print(time)
    print(name)

    with open(first_file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([time, name])




search()



