from django.contrib import admin

from .models import Weather


class WeatherAdmin(admin.ModelAdmin):
    display_list = ['city_name']


admin.site.register(Weather, WeatherAdmin)
