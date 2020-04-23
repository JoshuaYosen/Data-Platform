from bs4 import BeautifulSoup
import re
import urllib.request
import os.path


#searches current directory to see if file exists
def search(url):
    if os.path.isfile('{}_survey.csv'.format(date)):
        return True
    else:
        return False




#url = "https://insights.stackoverflow.com/survey"

#scrapes url to gather url information
def scrape(url):
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'htlm.parser')
    finder = soup.find_all('a')
    return finder

#collects date and url link from scraped data
def data(finder):
    for f in finder:
        data = [[f.attrs['data-year'], f.attrs['href']]]
    return data

#downloads data into date-stamped files
def download(data):
    for item in range(len(data)):
        url = data[item][1]
        date = data[item][0]
        while search(url) is False:
            print('Initiating {} Stack Overflow Survey donwload...'.format(date))

            urlib.request.urlretreive(url, '/home/j_yosen/Connect/{}_survey.csv'.format(date))

            print('Download Complete. Have a nice day :)')
