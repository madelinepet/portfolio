from django.urls import path
from .views import game_view, nasa_view, feedback_view
# vis_view

urlpatterns = [
    # path('vis', vis_view.as_view(), name='vis'),
    path('feedback', feedback_view, name='feedback'),
    path('game', game_view, name='game'),
    path('nasa', nasa_view.as_view(), name='nasa'),
]
