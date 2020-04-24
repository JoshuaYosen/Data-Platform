from api_v2 import *
import pytest
import requests


@pytest.fixture
def input_value():
    url = "https://insights.stackoverflow.com/survey"
    api = SO_Survey_API(url)
    return api



@pytest.fixture
def test_get_page(input_value):
    assert api.get_page(url)


@pytest.fixture
def test_get_surveys(test_get_page):
    assert api.get_surveys()


def test_donwload(test_get_surveys):
    assert api.download()
