import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"
bot = Bot(token=TOKEN)

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# --- أوامر البوت ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً بك في البوت!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("استخدم /start للبدء 😊")

# --- مسار الصفحة الرئيسية ---
@app.route("/", methods=["GET"])
def home():
    return "✅ البوت شغّال على Render!"

# --- مسار Webhook ---
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    if not application.initialized:
        await application.initialize()
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return "ok"

# --- تشغيل التطبيق ---
if __name__ == "__main__":
    # ربط الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # تعيين Webhook
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    asyncio.run(application.bot.set_webhook(webhook_url))

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
