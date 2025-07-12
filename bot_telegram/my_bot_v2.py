import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن من متغير البيئة (أو ضعه مباشرة بين "")
TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# الأوامر
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحبًا بك! هذا البوت يعمل بنجاح.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❓ استخدم /start للبدء.")

# إضافة الهاندلرز
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

# مسار الاستقبال من Telegram
@app.post(f"/{TOKEN}")
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    await application.initialize()
    await application.process_update(update)
    return "ok"

@app.get("/")
def home():
    return "✅ البوت شغال!"

# عند التشغيل
if __name__ == '__main__':
    async def run():
        # تعيين Webhook
        url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
        await application.bot.set_webhook(url)
        print(f"✅ Webhook set to: {url}")

        # تشغيل Flask
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

    asyncio.run(run())
