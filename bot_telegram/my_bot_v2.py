import os
import asyncio
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Application, ContextTypes

TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"
bot = Bot(token=TOKEN)
app = Flask(__name__)

# أوامر البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا بك!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("استخدم /start للبدء.")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application = app.config.get('application')
    if application:
        asyncio.get_event_loop().run_until_complete(application.process_update(update))
    return "ok"

@app.route('/', methods=['GET'])
def home():
    return "✅ البوت يعمل."

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # إعداد Webhook
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    asyncio.run(application.bot.set_webhook(webhook_url))

    app.config['application'] = application

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
