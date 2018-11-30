from django.urls import path
from .views import vis_view

urlpatterns = [
    path('vis', vis_view, name='vis'),
]
