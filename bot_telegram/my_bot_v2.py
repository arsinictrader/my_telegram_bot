from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"

app = Flask(__name__)

# أوامر البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """بقدملك في القناة..

_ اولا وأهم حاجه محتوي تعليمي قادر يحولك من مبتدأ لشخص قادر يعتمد علي نفسه وياخد صفقات❤️

_ جلسات تحليل يوميا مع صفقات مدروسة بعناية👌❤️

_ لايفات اسبوعيه مع الفريق لشرح استراتيجيات جديدة❤️

_ خطط مخصصة لكل شخص لأدارة رأس ماله بطريقة صحيحة👌❤️

_ متابعه بشكل يومي مع كامل اعضاء الفريق لتحقيق نتائج ممتازة👌❤️

رابط القناة تفضل للانضمام..

https://t.me/Arsenic_Trader0"""
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📌 أرسل /start لعرض محتوى القناة ورابط الانضمام.")

@app.route(f'/{TOKEN}', methods=['POST'])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return "ok"

@app.route('/', methods=['GET'])
def home():
    return "✅ البوت يعمل الآن."

if __name__ == '__main__':
    bot = Bot(token=TOKEN)
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # إعداد Webhook عند الإطلاق
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    asyncio.run(application.bot.set_webhook(webhook_url))

    port = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=port)
