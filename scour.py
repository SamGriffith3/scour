import requests
from bs4 import BeautifulSoup
import _csv as csv


def search():
    # Determine the location to be searched
    #city = input("Your Town/City: ")   Put this in later to replace "town" variable
    town = "greenville"
    craigslist = 'http://' + town + ".craigslist.org/search/zip"
    print(craigslist)
    r = requests.get(craigslist).text

    # Scraping the site
    first_file = "C:\\Users\\Sam\\Documents\\first.csv"

    for pg in craigslist:
        soup = BeautifulSoup(r, 'html.parser')
        name_box = soup.find('a', attrs={'class': 'result-title hdrlnk'}) # see below
        time_box = soup.find('time', attrs={'class': 'result-date'})  # need to find a way to get iterate thru
        name = name_box.text
        time = time_box.text
        data = []
        data.append((name, time))
        not_dup = []
        if name != not_dup:
            not_dup.append(name)
            with open(first_file, 'a') as csv_file:
                writer = csv.writer(csv_file)
                for name, time in data:
                    writer.writerow([time, name])
            print(time, name)
        else:
            continue


    print("done")


search()



