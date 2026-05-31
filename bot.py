from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🌐 الموقع", url="https://bahjaja.wuiltstore.com/")],
        [InlineKeyboardButton("📝 تقديم شكوى", url="https://forms.gle/Rk388FAJRhgWRW6r7")],
        [InlineKeyboardButton("📱 تنزيل التطبيق", url="https://apkpure.com/ar/bahjaja-store/co.median.android.krxwerj")],
        [InlineKeyboardButton("💬 التواصل معنا", callback_data="contact")]
    ]

    await update.message.reply_text(
        "مرحباً بك في بهججة ❤️\n\nاختر الخدمة المطلوبة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "contact":
        await query.message.reply_text(
            "أهلاً بك 👋\n\nاكتب رسالتك وسنقوم بإضافة الذكاء الاصطناعي لاحقاً."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
