from django.shortcuts import render
from django.views.generic import ListView
from .models import News
import os
import geocoder
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page
# from django.core.paginator import Paginator
# from django.conf import settings
g = geocoder.ip('me')
# import json
# import dateutil.parser
# from .news import get_news, analyze

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @cache_page(CACHE_TTL)
class vis_view(ListView):
    """ This is the function defining the list view of all articles. Context
    is sent to the template and can be accessed there
    """
    def get(self, request):
        # convert queryset to list so it's iterable
        articles = list(News.objects.all())
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
