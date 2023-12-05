import requests
from keys_settings import settings
from cachetools import TTLCache
from pydantic import BaseModel

ya_geocode_maps_url = settings['YA_GEOCODE_MAPS_URL']
cache = TTLCache(maxsize=100, ttl=30 * 60)


class WeatherData(BaseModel):
    temperature: float
    pressure: int
    wind_speed: float


def get_yandex_geocode_data(ya_geocode_api_key, city_name):
    """
        Функция, получающая координаты по названию города.
    """

    params = {
        'apikey': ya_geocode_api_key,
        'format': 'json',
        'geocode': city_name,
    }

    response = requests.get(ya_geocode_maps_url, params=params)
    data = response.json()

    try:
        point = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = map(float, point.split())
        return {'latitude': latitude, 'longitude': longitude}
    except (KeyError, IndexError):
        return None


def get_cache_key(city: str) -> str:
    return f'weather_{city}'


def get_cached_weather_data(city: str):
    return cache.get(get_cache_key(city))


def set_cached_weather_data(city: str, data):
    cache[get_cache_key(city)] = data
