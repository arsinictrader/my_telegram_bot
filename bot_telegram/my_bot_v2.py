import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن من المتغير البيئي
TOKEN = os.environ.get("BOT_TOKEN")

# إنشاء البوت و Flask
bot = Bot(token=TOKEN)
app = Flask(__name__)

# المعالجات (Handlers)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحبا بك! هذا بوت يعمل على Render.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("استخدم /start للبدء.")

# نقطة استقبال Webhook
@app.post(f"/{TOKEN}")
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    # نأخذ التطبيق من config
    application: Application = app.config['application']

    # تهيئة البوت
    await application.bot.initialize()

    # تمرير التحديث إلى التطبيق
    await application.process_update(update)

    return "OK"

# صفحة اختبار
@app.get("/")
def home():
    return "✅ البوت يعمل!"

# نقطة البداية
async def main():
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()

    # ربط المعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # إعداد Webhook
    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}"
    await application.bot.set_webhook(webhook_url)

    # حفظ التطبيق في Flask config
    app.config['application'] = application

    # تشغيل Flask
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# تشغيل البوت
if __name__ == "__main__":
    asyncio.run(main())
