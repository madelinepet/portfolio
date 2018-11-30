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

    return(response.json()['articles'])


def get_link():
    """ Specifically gets the info needed from the array of objects returned 
    from the get_news function, saves info to db in same for loop
    """
    res_list = get_news()
    link_list = []
    for article in res_list:
        link_list.append(article['url'])
    return(link_list)


def extract():
    """ Extracts the text from the urls's list returned from the get_link 
    function
    """
    links = get_link()
    all_articles_text = []
    for link in links:
        g = Goose()
        try:
            article = g.extract(link)
        except goose3.network.NetworkError:
            return False
        all_articles_text.append(article.cleaned_text)
    return all_articles_text


def analyze():
    """ Analyzes the text using the IBM Watson tone-analysis api
    """
    all_articles = extract()
    tone_analyzer = ToneAnalyzerV3(
                version='2017-09-21',
                iam_apikey=os.environ.get('IAM_APIKEY'),
                url='https://gateway.watsonplatform.net/tone-analyzer/api')

    for article in all_articles:
        return(tone_analyzer.tone(
                {'text': article},
                'application/json'))
