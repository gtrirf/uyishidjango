from django.urls import path
from home.views import print_hello, print_salom


urlpatterns = [
    path('hello/', print_hello),
    path('salom/', print_salom)
]