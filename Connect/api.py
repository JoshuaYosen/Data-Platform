from bs4 import BeautifulSoup
import re
import requests
import urllib
import os.path


#scrapes url to gather url information
def scrape():

    url = requests.get("https://insights.stackoverflow.com/survey")

    if urlib.urlopen(url).getcode() == 200:
        soup = BeautifulSoup(url.text, "html.parser")
        global finder
        finder = soup.find_all('a', href = re.compile(r'https://drive.google.com'))

    else:
        raise Exception("Host Could Not be Found")


#collects date and url link from scraped data
def get_data():

    global urls
    urls = [[f.attrs['data-year'], f.attrs['href']] for f in finder]


#downloads data into date-stamped files
def download():
    for item in range(len(urls)):
        url = urls[item][1]
        date = urls[item][0]

        if os.path.exists('/home/j_yosen/Data_Platform/Connect/Surveys/{}_survey.csv'.format(date)):
            print("The {} Survey already exists".format(date) + "\n")


        else:

            print('<Initiating {} Stack Overflow Survey Download>'.format(date) + "\n")

            file = requests.get(url)



            with open('/home/j_yosen/Data_Platform/Connect/Surveys/{}_survey.csv'.format(date), 'wb') as f:
                f.write(file.content)

            print('***BEEP BOOP*** {} Survey Download Complete. Have a nice day :)'.format(date) + "\n")



    print("Process Complete. You are up to date" + "\n")

if __name__ == '__main__':
    url = "https://insights.stackoverflow.com/survey"
    scrape()

    get_data()

    download()
