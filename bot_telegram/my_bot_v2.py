import os
import asyncio
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN مفقود! أضفه إلى متغيرات البيئة.")

bot = Bot(token=TOKEN)
app = Flask(__name__)

# دوال الأوامر
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """بقدملك في القناة..

_ محتوى تعليمي قوي ✅
_ جلسات تحليل يومي ✅
_ لايفات واستراتيجيات ✅
_ خطط إدارة رأس المال ✅

رابط القناة:
https://t.me/Arsenic_Trader0"""
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📌 أرسل /start لعرض محتوى القناة ورابط الانضمام.")

# Webhook endpoint
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    app.application.create_task(app.application.process_update(update))
    return "ok"

@app.route('/', methods=['GET'])
def home():
    return "✅ البوت يعمل."

# التشغيل
if __name__ == "__main__":
    async def run():
        application = Application(token=TOKEN)

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))

        # ربط التطبيق بـ Flask
        app.application = application

        # إعداد Webhook
        webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
        await application.bot.set_webhook(url=webhook_url)
        print(f"🚀 Webhook set to: {webhook_url}")

        # تشغيل Flask
        port = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=port)

    asyncio.run(run())
