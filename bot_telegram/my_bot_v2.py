import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ⚠️ تأكد أنك أضفت BOT_TOKEN في إعدادات Render
TOKEN = os.environ.get("BOT_TOKEN")

# إعداد Flask و telegram-application
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# دالة start للرد على المستخدم
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "بقدملك في القناة..\n\n"
        "_ اولا وأهم حاجه محتوي تعليمي قادر يحولك من مبتدأ لشخص قادر يعتمد علي نفسه وياخد صفقات❤️_\n\n"
        "_ جلسات تحليل يوميا مع صفقات مدروسة بعناية👌❤️_\n\n"
        "_ لايفات اسبوعيه مع الفريق لشرح استراتيجيات جديدة❤️_\n\n"
        "_ خطط مخصصة لكل شخص لأدارة رأس ماله بطريقة صحيحة👌❤️_\n\n"
        "_ متابعه بشكل يومي مع كامل اعضاء الفريق لتحقيق نتائج ممتازة👌❤️_\n\n"
        "*رابط القناة تفضل للانضمام:*\n"
        "[اضغط هنا للانضمام](https://t.me/Arsenic_Trader0)"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# أضف المعالج
application.add_handler(CommandHandler("start", start))

# صفحة فحص بسيطة
@app.route("/")
def index():
    return "Bot is running!"

# webhook
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)

    # ✅ نتحقق أن التطبيق بدأ مرة واحدة فقط
    if not application.running:
        await application.initialize()
        await application.start()

    await application.process_update(update)
    return "OK"

# تشغيل البوت وتعيين الويب هوك
if __name__ == "__main__":
    async def main():
        await application.initialize()
        await application.bot.set_webhook(url=f"https://my-telegram-bot-qn6l.onrender.com/{TOKEN}")
        await application.start()
        app.run(host="0.0.0.0", port=10000)

    asyncio.run(main())
