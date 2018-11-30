# from goose3 import Goose
# import goose3
# import requests
# from watson_developer_cloud import ToneAnalyzerV3
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from .models import Article
# import os


# def connect_to_db(db_path):
#     """ Forms the db connection
#     """
#     my_engine = create_engine(db_path)
#     Session = sessionmaker(bind=my_engine)
#     return Session()


# def get_news():
#     """ API call to news api to get current news
#     """
#     url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=62d8cce09c5f447ea8d980720d63b3ef'
#     response = requests.get(url)
#     # TODO: add this to news_info column in the correct record

#     return(response.json()['articles'])


# def get_link():
#     """ Specifically gets the info needed from the array of objects returned from the get_news function, saves info to db in same for loop
#     """
#     res_list = get_news()
#     link_list = []
#     db_path = 'postgres://localhost:5432/news'

#     session = connect_to_db(db_path)
#     for article in res_list:
#         link_list.append(article['url'])
#         try:
#             article_to_insert = Article(title=article['title'], description=article['description'], source=article['source'], date_published=article['date_published'], url=article['url'], dom_tone=article['dom_tone'], image=article['image'])
#             article_exists = session.query(
#                 session.query(Article).filter_by(title=article['title']).exists()).scalar()
#             if not article_exists:
#                 session.add(article_to_insert)
#             else:
#                 session.commit()
#                 continue

#         except TypeError:
#                 continue
#     return(link_list)


# def extract():
#     """ Extracts the text from the urls's list returned from the get_link function
#     """
#     links = get_link()
#     all_articles_text = []
#     for link in links:
#         g = Goose()
#         try:
#             article = g.extract(link)
#         except goose3.network.NetworkError:
#             return False
#         all_articles_text.append(article.cleaned_text)
#     return all_articles_text


# def analyze():
#     """ Analyzes the text using the IBM Watson tone-analysis api
#     """
#     all_articles = extract()
#     tone_analyzer = ToneAnalyzerV3(
#                 version='2017-09-21',
#                 iam_apikey=os.environ.get('IAM_APIKEY'),
#                 url='https://gateway.watsonplatform.net/tone-analyzer/api')

#     for article in all_articles:
#         return(tone_analyzer.tone(
#                 {'text': article},
#                 'application/json'))
#         # TODO: add this to the db in the correct record


# def save():
#     """ saves to the db
#     """
    


    

#     # session.query(Article).delete()

# # TODO: commit to session
# # session.commit()