from django.shortcuts import render
# from .models import Article
import json
import dateutil.parser
from .news import get_news, analyze
import os
import geocoder
g = geocoder.ip('me')


def vis_view(request, data=None):
    """ This is the function defining the list view of all articles. Context 
    is sent to the template and can be accessed there
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
        # all_tones_per_article = []
        # try:
        #     for inditone in tones[data.index(article)].result['document_tone']['tones']:
        #         all_tones_per_article.append(inditone['tone_id'])
        #     new_entry.append({'dom_tone': ', '.join(all_tones_per_article)})
        # except AttributeError:
        #     pass
        context['articles'].append(new_entry)

    return render(request, 'news/vis.html', context)


def maps_view(request):
    """This is the function defining the map view.
    """
    if request.method == 'POST':
        map_manip = os.environ.get('MAPS_URL') + request.POST['search-map'] + '&center=' + request.POST['search-loc'] + '&zoom=13'

    else: 
        map_manip = os.environ.get('MAPS_DEFAULT') + '&center=' + str(g.latlng[0]) + ',' + str(g.latlng[1]) + '&zoom=3'
    context = {
        'maps': map_manip
    }
    return render(request, 'maps/maps.html', context)
