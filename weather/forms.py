from django.forms import ModelForm, TextInput
from .models import Weather


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['city_name']

        widgets = {
            'city_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter City Name',
                'id': 'city_name',
            })
        }
