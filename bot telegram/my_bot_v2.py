from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "🌿 البوت يعمل الآن على Render."

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

async def run_telegram_bot():
    app = ApplicationBuilder().token("7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("✅ البوت يعمل الآن... جربي إرسال /start أو /help.")
    await app.run_polling()

def start_bot():
    asyncio.run(run_telegram_bot())

if __name__ == '__main__':
    Thread(target=start_bot).start()
    app_flask.run(host="0.0.0.0", port=10000)
