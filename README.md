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


3. Запустить локально сервер:
    ```
    uvicorn main:app --reload 
    ```
#### Проверить АПИ можно по адресу http://127.0.0.1:8000/docs
(В параметре city можете запросить любой город)


4. Запустить телеграм бота:
    ```
    python tg_weather_bot.py
    ```
   
#### Найти бота в ТГ можно так https://t.me/fast_api_weather_echo_bot
