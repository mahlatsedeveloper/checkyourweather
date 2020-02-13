from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse

import requests
import json

from .models import Weather
from .forms import WeatherForm


def search_address(request):

    if request.method == 'POST':  # Check form if submitted
        form = WeatherForm(request.POST)
        if form.is_valid():
            city_name = request.POST.get('city_name')

            results_data = {}

            # Set Map Box url
            map_box_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json?access_token=pk.eyJ1IjoidnVraWxlIiwiYSI6ImNqaTA5eHdkYjEyZnUzd29lcml3d2R3bHQifQ.gKVTRsl2yTg1BEu3VPZAYg'

            # Requesting Map Box url details
            mapbox_r = requests.get(map_box_url).json()

            # Assign Latitude from mapbox_r
            latitude = mapbox_r['features'][0]['center'][0]
            # Assign Latitude from mapbox_r
            longitude = mapbox_r['features'][0]['center'][1]

            # Setup Darksky api with Lat and Long from Map box details
            url = f'https://api.darksky.net/forecast/7ca65b110e9f7a4676d6086908684808/{latitude},{longitude}'

            # Requesting Dark Sky url details
            darksky_r = requests.get(url).json()

            results_data['temperature'] = darksky_r['currently']['temperature']
            results_data['summary'] = darksky_r['currently']['summary']

            return HttpResponse(json.dumps(results_data), content_type="application/json")
    else:
        form = WeatherForm()

    context = {
        'form': form,
    }

    return render(request, 'weather/index.html', context)


def save_weather(request):

    if request.method == 'POST':
        form = WeatherForm(request.POST)

        if form.is_valid():
            add_weather = form.save(commit=False)
            city_name = request.POST.get('city_name')

            # Set Map Box url
            map_box_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json?access_token=pk.eyJ1IjoidnVraWxlIiwiYSI6ImNqaTA5eHdkYjEyZnUzd29lcml3d2R3bHQifQ.gKVTRsl2yTg1BEu3VPZAYg'

            # Requesting Map Box url details
            mapbox_r = requests.get(map_box_url).json()

            # Assign Latitude from mapbox_r
            latitude = mapbox_r['features'][0]['center'][0]
            # Assign Latitude from mapbox_r
            longitude = mapbox_r['features'][0]['center'][1]

            # Setup Darksky api with Lat and Long from Map box details
            url = f'https://api.darksky.net/forecast/7ca65b110e9f7a4676d6086908684808/{latitude},{longitude}'

            # Requesting Dark Sky url details
            darksky_r = requests.get(url).json()

            temperature = darksky_r['currently']['temperature']
            summary = darksky_r['currently']['summary']

            # Adding fields to the db
            add_weather.city_name = city_name
            add_weather.summary = summary
            add_weather.temperature = temperature

            add_weather.save()
    else:
        form = WeatherForm()

    context = {
        'form': form,
    }

    return render(request, 'weather/index.html', context)


def retrieve_weather(request):
    results = Weather.objects.all()

    if request.method == 'GET':
        json_results = serializers.serialize("json", results)
        json_result = json.loads(json_results)

        return HttpResponse(json.dumps(json_result), content_type="application/json")
