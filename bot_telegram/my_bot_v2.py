import os
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

TOKEN = "ضع_توكن_البوت_هنا"  # 🔁 استبدله بتوكن البوت الحقيقي

# أوامر البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أنا بوتك جاهز 🚀")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("استخدم /start للبدء 💡")

# نقطة البداية
async def main():
    # بناء التطبيق
    app = Application.builder().token(TOKEN).build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # إعداد Webhook
    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}"
    await app.bot.set_webhook(webhook_url)

    print(f"✅ Webhook set to: {webhook_url}")

    # تشغيل السيرفر الداخلي لـ telegram-bot
    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_path=f"/{TOKEN}",
    )

# لتشغيل الكود
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
