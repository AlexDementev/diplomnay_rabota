from django.urls import path

from . import views
from .views import  catalog_page

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
path('profile/', views.profile),
    path('catalog/', catalog_page, name='catalog'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', views.login),
    path('authorize/', views.authorize),
    path('search/', views.search),
    path('registration/', views.registration),
]
