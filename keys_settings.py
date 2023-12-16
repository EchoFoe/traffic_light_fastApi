from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
GEOCODE_API_KEY = os.environ.get('GEOCODE_API_KEY')
YA_GEOCODE_MAPS_URL = os.environ.get('YA_GEOCODE_MAPS_URL')
WEATHER_API_URL = os.environ.get('WEATHER_API_URL')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_BOT_NAME = os.environ.get('TELEGRAM_BOT_NAME')

