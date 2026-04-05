import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

# --- SETTINGS ---
API_TOKEN = '7921854103:AAGoZs7ZQqSOO90exsfo18NPbWw4_1_ILto' # Replace with your token
# Replace with the link you get from GitHub Pages (Settings -> Pages)
APP_URL = "https://vluxx17-creator.github.io/Betatest/" 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
  # Keyboard with the button to open the Mini App
  markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
      text="🚀 Открыть Поиск", 
      web_app=WebAppInfo(url=APP_URL)
    )],
    [InlineKeyboardButton(
      text="Помощь", 
      callback_data="help"
    )]
  ])
  
  await message.answer(
    f"Привет, {message.from_user.first_name}!\n"
    "Нажми на кнопку ниже, чтобы запустить Mini App:",
    reply_markup=markup
  )

# Handler for data coming FROM the Mini App
@dp.message(F.web_app_data)
async def web_app_data_handler(message: Message):
  # The data sent via tg.sendData(val) in index.html
  data = message.web_app_data.data
  await message.answer(f"✅ Вы ввели в Mini App: {data}")

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Bot stopped")
