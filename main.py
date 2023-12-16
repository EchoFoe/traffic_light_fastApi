import httpx

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

from keys_settings import WEATHER_API_URL, GEOCODE_API_KEY, WEATHER_API_KEY
from utils import WeatherData, get_yandex_geocode_data, get_cached_weather_data, set_cached_weather_data


app = FastAPI(title='Weather Ya API')


geocode_api_key = GEOCODE_API_KEY
weather_api_url = WEATHER_API_URL
weather_api_key = WEATHER_API_KEY


async def fetch_weather_data(city: str):
    # Получение координат по названию города
    geocode_data = get_yandex_geocode_data(geocode_api_key, city)

    if not geocode_data:
        raise HTTPException(status_code=500, detail=f'Невозможно получить данные для {city}')

    # Формирование параметров для корректного запроса к API Яндекс погода
    params = {'lang': 'ru_RU', 'lat': geocode_data['latitude'], 'lon': geocode_data['longitude']}
    headers = {'X-Yandex-API-Key': weather_api_key}

    async with httpx.AsyncClient() as client:
        try:
            # Запрос к API Яндекс погода
            response = await client.get(weather_api_url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            # Извлечение данных о погоде
            weather_data = {
                'temperature': data['temp'],
                'pressure': data['pressure_mm'],
                'wind_speed': data['wind_speed'],
            }
            # Сериализация данных о погоде
            serializer = WeatherData(**weather_data)

            # Установка кеша по названию города (30 минут) для исключения повторных запросов
            set_cached_weather_data(city, serializer.model_dump())

            return serializer.model_dump()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f'Ошибка получения данных: {str(e)}')


@app.get('/weather')
async def get_weather(city: str = Query(..., title='Название города')):
    # Закешируем город
    cached_weather_data = get_cached_weather_data(city)
    if cached_weather_data:
        return JSONResponse(content=cached_weather_data)

    # Получение данных о погоде
    weather_data = await fetch_weather_data(city)
    return JSONResponse(content=weather_data)
