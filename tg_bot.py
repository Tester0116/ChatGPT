import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

openai.api_key = '' // OpenAI API-KEY
token = '' // tg-bot_token

bot = Bot(token)
dp = Dispatcher(bot)

def update(messages, role, content):
    messages.append({"role":role, "content":content})
    return messages

# обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, я бот! Я могу отвечать на ваши сообщения.")

@dp.message_handler()
async def send(message : types.Message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a helpful assistant"},
        {"role":"user","content":"/start"},
        {"role":"assistant","content":"Hello Nurick"},
        {"role":"user","content":message.text},
    ]
)

    await message.answer(response['choices'][0]['message']['content'])

executor.start_polling(dp, skip_updates=True)
