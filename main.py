from os import environ
from pyrogram import Client
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)



api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
info = "Greetings from **Heroku**!"

app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
print(info)

@app.on_message()
async def work(client, message):
    await app.send_message(message.chat.id, info)
    await app.send_message(message.chat.id, "These are inline buttons",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Data", callback_data="callback_data")],
            [InlineKeyboardButton("Docs", url="https://docs.pyrogram.org")]
        ]))

   @app.send_photo(
    chat_id=message.chat.id,
    photo=photo
)
async def work(client, message):
await app.message.reply_photo(https://telegra.ph/file/aa59c3024666f7bc9f712.jpg)
app.run()
