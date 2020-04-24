from bs4 import BeautifulSoup
import re
import requests
import urllib
import os.path


#class for donwloading surveys from Stack Overflow Insights
class SO_Survey_API():
    def __init__(self, url):
        self.url = requests.get(url)


    #creates a BeautifulSoup object from website
    def get_page(self):
        self.soup = BeautifulSoup(self.url.text, "html.parser")
        return self.soup

    #retrieves list of dates and urls for each survey
    def get_surveys(self, regex):
        finder = self.soup.find_all('a', href = re.compile(regex) )
        self.urls = [[f.attrs['data-year'], f.attrs['href']] for f in finder]

        print(self.urls)
        return self.urls


    #downloads surveys into file of choice 
    def download(self, path):

        for item in range(len(self.urls)):
            url = self.urls[item][1]
            date = self.urls[item][0]

            if os.path.exists(path + '{}_survey.csv'.format(date)):
                print("The {} Survey already exists".format(date) + "\n")


            else:

                print('<Initiating {} Stack Overflow Survey Download>'.format(date) + "\n")

                file = requests.get(url)



                with open(path + '{}_survey.csv'.format(date), 'wb') as f:
                    f.write(file.content)

                print('***BEEP BOOP*** {} Survey Download Complete. Have a nice day :)'.format(date) + "\n")



        print("Process Complete. You are up to date" + "\n")



if __name__ == "__main__":
    api = SO_Survey_API(url="https://insights.stackoverflow.com/survey")
    api.get_page()
    api.get_surveys(regex= r'https://drive.google.com')
    api.download(path = '/home/j_yosen/Documents/')
