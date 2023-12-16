from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from keys_settings import TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_NAME
from main import fetch_weather_data

bot = Bot(token=f'{TELEGRAM_BOT_TOKEN}')
dp = Dispatcher(bot)
telegram_bot_name = TELEGRAM_BOT_NAME


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    welcome_message = f'Добро пожаловать в {telegram_bot_name}! ' \
                      f'Для получения погоды используйте кнопку "Узнать погоду".'
    keyboard = InlineKeyboardMarkup()
    show_weather_button = InlineKeyboardButton('Узнать погоду', callback_data='show_weather')
    # exit_button = InlineKeyboardButton('Выйти', callback_data='exit')
    keyboard.add(show_weather_button)
    await message.answer(welcome_message, reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'show_weather')
async def show_weather_callback(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id)
    await bot.send_message(query.from_user.id, 'Введите название города')


@dp.callback_query_handler(lambda c: c.data == 'exit')
async def exit_callback(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id)
    await send_welcome(query.message)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: Message):
    try:
        city = message.text
        weather_data = await fetch_weather_data(city)
        weather_info = (
            f"Погода в {city.capitalize()}:\n"
            f"Температура: {weather_data['temperature']}°C\n"
            f"Давление: {weather_data['pressure']} мм. рт. ст.\n"
            f"Скорость ветра: {weather_data['wind_speed']} м/с"
        )

        keyboard = InlineKeyboardMarkup()
        exit_button = InlineKeyboardButton('Выйти', callback_data='exit')
        keyboard.add(exit_button)

        await message.answer(weather_info, reply_markup=keyboard)
    except Exception as e:
        await message.answer(f'Ошибка {str(e)}')


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
