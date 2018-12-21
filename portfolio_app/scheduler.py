#!/usr/bin/python
from django_cron import CronJobBase, Schedule
from goose3 import Goose
import goose3
from watson_developer_cloud import ToneAnalyzerV3
from .news import get_news
import os
# from .models import News


import psycopg2


def extract_text(url):
    """Function to extract text from article
    """
    g = Goose()

    try:
        article = g.extract(url)
    except goose3.network.NetworkError:
        return False

    return article.cleaned_text


def analyze_text(text):
    tone_analyzer = ToneAnalyzerV3(
                version='2017-09-21',
                iam_apikey=os.environ.get('IAM_APIKEY'),
                url='https://gateway.watsonplatform.net/tone-analyzer/api')

    return tone_analyzer.tone(
            {'text': text},
            'application/json')


class MyCronJob(CronJobBase):
    """ Responsible for everything related to my chron job itself
    """
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'portfolio_app.my_cron_job'

    def do(self):
        """ cron job using psycopg2
        """
        conn = psycopg2.connect("dbname=madelinepet")
        cur = conn.cursor()
        api_response = get_news()

        parsed_article_list = []

        for obj in api_response:
            parsed_article = {
                'title': obj['title'],
                'url': obj['url'],
                'description': obj['description'],
                'source': obj['source']['name'],
                'date_published': obj['publishedAt'],
                'image': obj['urlToImage'],
                }
            parsed_article_list.append(parsed_article)

        analyzed_articles = []

        for article in parsed_article_list:
            url = article['url']

            text = extract_text(url)
            if not text:
                continue

            tone_analysis = analyze_text(text).get_result()

            if len(tone_analysis['document_tone']['tones']):
                dom_tone = tone_analysis['document_tone']['tones'][-1]['tone_name']
                article = {
                    'title': article['title'],
                    'url': article['url'],
                    'description': article['description'],
                    'source': article['source'],
                    'date_published': article['date_published'],
                    'image': article['image'],
                    'dom_tone': dom_tone
                    }
                analyzed_articles.append(article)

                try:
                    cur.execute("INSERT INTO portfolio_app_news (title, url, description, source, date_published, image, dom_tone) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (article['title'], article['url'], article['description'], article['source'], article['date_published'], article['image'], article['dom_tone']))
                    conn.commit()
                    print('success')
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                    continue

        conn.commit()
        cur.close()
        conn.close()
