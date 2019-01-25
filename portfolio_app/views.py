from django.shortcuts import render
import os
import requests
from .models import Image
from .forms import ImageForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
import geocoder
g = geocoder.ip('me')



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
        """ atattches the user's images to the ctx obj to be used in template
        """
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
        """ Adds the user and the url to the image on submit
        """
        nasa_url = os.environ.get('NASA_URL')
        response = requests.get(nasa_url)
        data = response.json()
        image_otd = data['url']
        form.instance.user = self.request.user
        form.instance.url = image_otd
        return super().form_valid(form)

# add users field to Image model and have an array in there. If the user is in there for that image, display the image to them
# have url be unique and if IntegrityError, just add user to array in users
