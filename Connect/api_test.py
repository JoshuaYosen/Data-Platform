from bs4 import BeautifulSoup
import requests
import re



def test_scrape_function():
    url = requests.get("https://insights.stackoverflow.com/survey")
    soup = BeautifulSoup(url.text, "html.parser")
    finder = soup.find_all('a', href = re.compile(r'https://drive.google.com'))


    urls = [[f.attrs['data-year'], f.attrs['href']] for f in finder]
    dates = [f.attrs['data-year'] for f in finder]

    print(urls)










if __name__ == "__main__":
    test_scrape_function()
