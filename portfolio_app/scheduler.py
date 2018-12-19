from django_cron import CronJobBase, Schedule
from goose3 import Goose
import goose3
import requests
from watson_developer_cloud import ToneAnalyzerV3
import os
from .news import get_news, analyze
import dateutil.parser
# import psycopg2
# from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmake
from .models import News


def connect_to_db(db_path):
    """This function creates an engine and a session, allowing 
    sqlalchemy to connect to the db.
    """
    my_engine = create_engine(db_path)

    # create a configured "Session" class
    Session = sessionmaker(bind=my_engine)

    # create a Session
    return Session()


def fetch_news(): 
    """ Grabs the news from the api
    """
    data = get_news()
    tones = []
    for article in get_news():
        try:
            tones.append(analyze(article))

        except Exception:
            tones.append(None)

    context = {
        'articles': []
    }

    for article in data:
        new_entry = []
        new_entry.append({'title': article['title']})

        new_entry.append({'description': article['description']})
        new_entry.append({'source': article['source']['name']})
        new_entry.append({'date_published': str(dateutil.parser.parse(article['publishedAt']))[:10]})
        new_entry.append({'url': article['url']})
        # append correct tone dict here
        all_tones_per_article = []
        try:
            for inditone in tones[data.index(article)].result['document_tone']['tones']:
                all_tones_per_article.append(inditone['tone_id'])
            new_entry.append({'dom_tone': ', '.join(all_tones_per_article)})
        except AttributeError:
            pass
        context['articles'].append(new_entry)


class MyCronJob(CronJobBase):
    """ Responsible for everything related to my chron job itself
    """
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'portfolio_app.my_cron_job'

    def do(self):
        """ Runs this fn every so often as defined above
        """
        # add db path into .env in ec2 config
        db_path = os.environ.get('DB_PATH')

        session = connect_to_db(db_path)

        session.query(News).delete()
        session.commit()
        # not finished

