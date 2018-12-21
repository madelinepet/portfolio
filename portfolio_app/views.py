from django.shortcuts import render
from django.views.generic import ListView
from .models import News
import os
import geocoder
import dateutil.parser
g = geocoder.ip('me')


class vis_view(ListView):
    """ This is the function defining the list view of all articles. Context
    is sent to the template and can be accessed there. Convert queryset to 
    list so it's iterable
    """
    def get(self, request):
        articles = list(News.objects.all())
        for article in articles:
            article.date_published = str(dateutil.parser.parse(article.date_published))[:10]

        context = {
            'articles': articles
        }
        return render(request, 'news/vis.html', context)


def maps_view(request):
    """This is the function defining the map view.
    """
    if request.method == 'POST':
        if ' ' in request.POST:
            request.POST.split(' ')
            '+'.join(request.POST)

        map_manip = os.environ.get('MAPS_URL') + request.POST['search-map'] + request.POST['search-loc'] + '&zoom=11'

    else:
        map_manip = os.environ.get('MAPS_DEFAULT') + '&center=' + str(g.latlng[0]) + ',' + str(g.latlng[1]) + '&zoom=3'
    context = {
        'maps': map_manip
    }
    return render(request, 'maps/maps.html', context)
