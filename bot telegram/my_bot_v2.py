from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

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

def run_bot():
    app = ApplicationBuilder().token("7574658871:AAGoPVLsmrkYVUNWimZWOPcontuLXGYyiU4").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("✅ البوت يعمل الآن... جربي إرسال /start أو /help.")
    app.run_polling()

def run_server():
    PORT = 10000
    Handler = SimpleHTTPRequestHandler
    with TCPServer(("", PORT), Handler) as httpd:
        print(f"🌿 Running dummy server on port {PORT} to keep Render active.")
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_server()
