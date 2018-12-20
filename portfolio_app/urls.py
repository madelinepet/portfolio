from django.urls import path
from .views import vis_view, maps_view

urlpatterns = [
    path('vis', vis_view.as_view(), name='vis'),
    path('maps', maps_view, name='maps')
]
