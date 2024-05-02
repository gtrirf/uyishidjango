from django.urls import path
from .views import *


urlpatterns = [
    path('products/', get_info, name='get_info')
]