import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes

from telegram.ext import defaults  # مهم جدًا في بعض البيئات

# استخدم التوكن من البيئة
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN مفقود! ضعه في متغيرات البيئة في Render.")

bot = Bot(token=TOKEN)
app = Flask(__name__)

# دوال الأوامر
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

# Webhook endpoint
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application = app.config['application']
    application.create_task(application.process_update(update))
    return "ok"

@app.route('/', methods=['GET'])
def index():
    return "✅ البوت يعمل حالياً."

if __name__ == '__main__':
    import asyncio

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # إعداد Webhook تلقائيًا في Render
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    asyncio.run(application.bot.set_webhook(url=webhook_url))

    app.config['application'] = application

    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
