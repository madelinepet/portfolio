from django.urls import path
from .views import maps_view, game_view, nasa_view
# vis_view

urlpatterns = [
    # path('vis', vis_view.as_view(), name='vis'),
    path('maps', maps_view, name='maps'),
    path('game', game_view, name='game'),
    path('nasa', nasa_view, name='nasa'),
]
