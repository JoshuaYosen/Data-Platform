from api import *
import pytest
import urllib


@pytest.fixture
def input_value():
    url = requests.get("https://insights.stackoverflow.com/survey")
    return url



def test_scrape(input_value):

    if urlib.urlopen(url).getcode() == 200:
        soup = BeautifulSoup(url.text, "html.parser")
        global finder
        finder = soup.find_all('a', href = re.compile(r'https://drive.google.com'))
        assert finder


    else:
        raise Exception("Host Could Not be Found")

def test_get_data():
    global urls
    assert urls == [[f.attrs['data-year'], f.attrs['href']] for f in finder]


def test_donwload():
    for item in range(len(urls)):
        url = urls[item][1]
        date = urls[item][0]

        if os.path.exists('/home/j_yosen/Data_Platform/Connect/Surveys/{}_survey.csv'.format(date)):
            assert print("The {} Survey already exists".format(date) + "\n")


        else:

            assert print('<Initiating {} Stack Overflow Survey Download>'.format(date) + "\n")

            file = requests.get(url)



            with open('/home/j_yosen/Data_Platform/Connect/Surveys/{}_survey.csv'.format(date), 'wb') as f:
                assert f.write(file.content)

            assert print('***BEEP BOOP*** {} Survey Download Complete. Have a nice day :)'.format(date) + "\n")



    assert print("Process Complete. You are up to date" + "\n")
