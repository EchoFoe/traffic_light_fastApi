## Инструкция по локальному развертыванию проекта

Для работы проекта потребуются:

- Python
- FastApi
- aiogram
    
Проект содержит в себе requirements.txt


1. Клонировать проект:
    ```
    git clone https://github.com/EchoFoe/traffic_light_fastApi.git
    ```

2. Создать виртуальную среду и установить в неё зависимости:
    ```
    pip install -r requirements.txt
    ```

3. Создать файл .env в корне проекта и занести туда следующие константы:
    ```
   WEATHER_API_KEY=<your_api_key_from_yandex_api_pogoda>
   GEOCODE_API_KEY=<your_api_key_from_yandex_http_geocoder>
   TELEGRAM_BOT_TOKEN=<your_token_bot_from_telegram>
   TELEGRAM_BOT_NAME=<your_name_bot_from_telegram>
   YA_GEOCODE_MAPS_URL=https://geocode-maps.yandex.ru/1.x/
   WEATHER_API_URL=https://api.weather.yandex.ru/v2/fact?
    ```

4. Запустить локально сервер:
    ```
    uvicorn main:app --reload 
    ```
#### Проверить АПИ можно по адресу http://127.0.0.1:8000/docs
(В параметре city можете запросить любой город)


5. Запустить телеграм бота:
    ```
    python tg_weather_bot.py
    ```
