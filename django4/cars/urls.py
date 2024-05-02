from django.urls import path
from .views import get_info, get_cars, detail


urlpatterns = [
    path('', get_info, name='get_info'),
    path('cars/<int:pk>', get_cars, name='get_cars'),
    path('cars/detail/<int:pk>', detail, name='detail')
]