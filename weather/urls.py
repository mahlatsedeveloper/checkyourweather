from django.conf.urls import url

from . import views


app_name = 'weather'

urlpatterns = [
    url(r'^$', views.search_address, name='search_address'),
    url(r'^save-weather/',  views.save_weather, name='save_weather'),
    url(r'^retrieve-weather/', views.retrieve_weather, name='retrieve_weather'),
]
