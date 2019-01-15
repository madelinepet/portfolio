from django.urls import path
from .views import vis_view, maps_view, game_view

urlpatterns = [
    path('vis', vis_view.as_view(), name='vis'),
    path('maps', maps_view, name='maps'),
    path('game', game_view, name='game'),
]
