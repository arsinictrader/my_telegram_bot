import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Dispatcher

TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"

app_flask = Flask(__name__)
telegram_app = ApplicationBuilder().token(TOKEN).build()

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

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))

@app_flask.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return "OK"

@app_flask.route("/")
def index():
    return "🌿 البوت يعمل الآن باستخدام Webhook."

if __name__ == "__main__":
    # إعداد Webhook
    webhook_url = f"https://my-telegram-bot-t9qk.onrender.com/{TOKEN}"
    import asyncio
    asyncio.run(telegram_app.bot.set_webhook(url=webhook_url))
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
