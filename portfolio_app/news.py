from goose3 import Goose
import goose3
import requests
from watson_developer_cloud import ToneAnalyzerV3
import os


def get_news():
    """ API call to news api to get current news
    """
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=62d8cce09c5f447ea8d980720d63b3ef'
    response = requests.get(url)
    data = response.json()['articles']
    return(data)


def get_link():
    """ Specifically gets the info needed from the array of objects returned 
    from the get_news function, saves info to db in same for loop
    """
    res_list = get_news()
    link_list = []
    for article in res_list:
        link_list.append(article['url'])
    return(link_list)


def extract(article):
    """ Extracts the text from the urls's list returned from the get_link 
    function
    """
    link = article['url']
    g = Goose()
    try:
        article = g.extract(link)
    except goose3.network.NetworkError:
        return False

    return article.cleaned_text


def analyze(article):
    """ Analyzes the text using the IBM Watson tone-analysis api
    """
    text = extract(article)
    tone_analyzer = ToneAnalyzerV3(
                version='2017-09-21',
                iam_apikey=os.environ.get('IAM_APIKEY'),
                url='https://gateway.watsonplatform.net/tone-analyzer/api')

    return(tone_analyzer.tone(
                {'text': text},
                'application/json'))
