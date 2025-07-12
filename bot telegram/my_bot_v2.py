import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7574658871:AAHmLGQqI6r8J-gCc7NB4MsFZf2IIxOXjkc"
WEBHOOK_URL = f"https://my-telegram-bot-t9qk.onrender.com/{TOKEN}"

bot = Bot(TOKEN)
app_flask = Flask(__name__)

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

@app_flask.route(f'/{TOKEN}', methods=['POST'])
def webhook_handler():
    update = Update.de_json(request.get_json(force=True), bot)
    application = app_flask.config['application']
    application.create_task(application.process_update(update))
    return 'OK'

@app_flask.route('/', methods=['GET'])
def home():
    return '✅ البوت يعمل الآن على Render باستخدام Webhook.'

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # إعداد Webhook
    import asyncio
    asyncio.run(bot.set_webhook(WEBHOOK_URL))

    # تخزين التطبيق داخل flask config ليستخدمه webhook_handler
    app_flask.config['application'] = application

    # تشغيل Flask
    port = int(os.environ.get('PORT', 10000))
    app_flask.run(host='0.0.0.0', port=port)
