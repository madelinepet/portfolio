from django.shortcuts import render
import requests
# from .models import Article


def get_news():
    """ API call to news api to get current news
    """
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=62d8cce09c5f447ea8d980720d63b3ef'
    response = requests.get(url)
    data = response.json()['articles']
    return(data)


def vis_view(request, data=None):
    """ This is the function defining the list view of all articles. Context 
    is sent to the template and can be accessed there
    """
    data = get_news()

    context = {
        'articles': []
    }

    for article in data:
        new_entry = []
        new_entry.append({'title': article['title']})
        new_entry.append({'description': article['description']})
        new_entry.append({'source': article['source']['name']})
        new_entry.append({'date_published': article['publishedAt']})
        new_entry.append({'url': article['url']})
        context['articles'].append(new_entry)

    return render(request, 'news/vis.html', context)
