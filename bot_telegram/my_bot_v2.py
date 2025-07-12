import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")  # أو ضع التوكن مباشرة: TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"

bot = Bot(token=TOKEN)
app = Flask(__name__)

# تعريف أوامر البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحباً! أنا بوتك على Render.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❓ أرسل /start للبدء.")

# نقطة استقبال Webhook من Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    await app.application.process_update(update)
    return "ok"

# تأكيد أن السيرفر يعمل
@app.route("/", methods=["GET"])
def home():
    return "✅ البوت يعمل على Render!"

async def main():
    # إعداد التطبيق
    application = Application.builder().token(TOKEN).build()
    app.application = application  # نربطها بـ Flask

    # أوامر البوت
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # تعيين Webhook
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    await bot.set_webhook(webhook_url)
    print("✅ Webhook set to:", webhook_url)

    # تشغيل Flask
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    asyncio.run(main())
