import os
import asyncio
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ضع التوكن الخاص بك هنا
TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"
bot = Bot(token=TOKEN)
app = Flask(__name__)

# أوامر البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحبا بك! أنا بوتك.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ استخدم /start للبدء.")

# Webhook endpoint
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print("📥 تم استقبال تحديث:", data)

    update = Update.de_json(data, bot)
    application = app.config['application']
    asyncio.get_event_loop().create_task(application.process_update(update))
    return "ok"

# صفحة اختبار
@app.route('/', methods=['GET'])
def home():
    return "✅ البوت يعمل بشكل جيد!"

if __name__ == '__main__':
    # إعداد التطبيق
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # ربط التطبيق بـ Flask
    app.config['application'] = application

    # إعداد Webhook
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    asyncio.run(application.bot.set_webhook(webhook_url))
    print(f"✅ Webhook set to: {webhook_url}")

    # تشغيل سيرفر Flask
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
