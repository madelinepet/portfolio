from django.shortcuts import render
import os
import requests
from .models import Image
from .forms import ImageForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# import geocoder
# g = geocoder.ip('me')
# import dateutil.parser
# from django.views.generic import ListView
# from .models import News


# class vis_view(ListView):
#     """ This is the function defining the list view of all articles. Context
#     is sent to the template and can be accessed there. Convert queryset to 
#     list so it's iterable
#     """
#     def get(self, request):
#         articles = list(News.objects.all())
#         for article in articles:
#             article.date_published = str(dateutil.parser.parse(article.date_published))[:10]

#         context = {
#             'articles': articles
#         }
#         return render(request, 'news/vis.html', context)


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


def game_view(request):
    """
    """
    return render(request, 'game/game.html')


class nasa_view(CreateView):
    """ This is the function defining the nasa image of the day view
    """
    template_name = 'nasa/nasa.html'
    context_object_name = 'images'
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('nasa')

    def get_form_kwargs(self):
        """ Gets the username
        """
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def get(self, request):
        url = os.environ.get('NASA_URL')
        response = requests.get(url)
        data = response.json()
        image_otd = data['url']

        username = self.request.user.get_username()
        user_images = Image.objects.filter(user__username=username)
        context = {
            'nasa': image_otd,
            'user_images': user_images,
        }
        return render(request, 'nasa/nasa.html', context)

    def form_valid(self, form):
        """ Adds the user to the image on submit
        """
        nasa_url = os.environ.get('NASA_URL')
        response = requests.get(nasa_url)
        data = response.json()
        image_otd = data['url']
        form.instance.user = self.request.user
        form.instance.url = image_otd
        # import pdb; pdb.set_trace()
        return super().form_valid(form)
