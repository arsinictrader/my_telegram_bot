import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")  # ضع التوكن في إعدادات Render كمتغير بيئة باسم BOT_TOKEN

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()


@app.route("/")
def index():
    return "Bot is running!"


@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    if request.method == "POST":
        data = request.get_json(force=True)
        update = Update.de_json(data, application.bot)

        if not application.running:
            await application.initialize()
            await application.start()

        await application.process_update(update)
        return "OK"
