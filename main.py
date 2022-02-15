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
    await app.send_document("https://t.me/c/1720035751/2", caption="document caption")



@app.on_message(filters.command("love"))
async def work(client, message):
    print("This is the /start command")

@app.on_message(filters.command(["startt"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hello there!",
        reply_to_message_id=update.message_id
    )

app.run()
