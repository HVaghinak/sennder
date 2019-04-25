import datetime

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework import serializers


class FetchGhibliMovieSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response_data = []
        self._generate_response()

    # TODO try to rewrite with asyncio
    def _get_data(self):
        data = requests.get(settings.GHIBLI_MOVIE_URL).json()
        for film in data:
            if not film.get('people'):
                self.response_data.append(film)
                continue
            if len(film['people']) > 1:
                peoples = []
                for people in film['people']:
                    people_data = requests.get(people).json()
                    peoples.append(people_data)
                film['people'] = peoples
            else:
                film['people'] = requests.get(film['people'][0]).json()
                self.response_data.append(film)

        current_url = self.context['request'].build_absolute_uri()
        caching_data = {
            'timestamp': datetime.datetime.now(),
            'data': self.response_data
        }
        cache.set(current_url, caching_data)

    @property
    def response(self):
        return self.response_data

    def _generate_response(self):
        current_url = self.context['request'].build_absolute_uri()
        cached_data = cache.get(current_url)

        if cached_data and (datetime.datetime.now() - cached_data['timestamp']).seconds < 60:
            self.response_data = cached_data['data']
        else:
            self._get_data()

