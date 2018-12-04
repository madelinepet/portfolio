from django.shortcuts import render
# from .models import Article
import dateutil.parser
from .news import get_news, analyze


def vis_view(request, data=None):
    """ This is the function defining the list view of all articles. Context 
    is sent to the template and can be accessed there
    """
    data = get_news()
    tone = analyze()
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
        new_entry.append(tone)
        context['articles'].append(new_entry)

    return render(request, 'news/vis.html', context)
