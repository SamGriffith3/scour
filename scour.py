import requests
from bs4 import BeautifulSoup
import os
import reusables
import getpass


def search():
    # Determine the location to be searched
    # city = input("Your Town/City: ")   Put this in later to replace "town" variable
    town = "greenville"

    item_type = "zip"  # Changing so can do link combination better later
    craigslist = 'http://' + town + ".craigslist.org/search/"

    r = requests.get(craigslist + item_type).text

    # Scraping the site
    first_file = "C:\\Users\\{}\\Documents\\first.csv".format(getpass.getuser()) # So it works on both mine and yours

    soup = BeautifulSoup(r, 'html.parser')

    data = []
    if os.path.exists(first_file):
        data = reusables.csv_to_list(first_file)  # Cheating because I already wrote this code

    for item in soup.find_all('li', attrs={"class": "result-row"}):
        a_link = item.find('a', attrs={'class': 'result-title hdrlnk'})
        datetime = item.find('time', attrs={'class': 'result-date'})['datetime']
        new_row = [datetime, a_link.text,
                   craigslist + a_link['href'].lstrip("/")]
        if new_row in data:
            continue
        data.append(new_row)
        print("Adding {}".format(a_link.text))

    reusables.list_to_csv(data[-50:], first_file)

    print("done")


search()
