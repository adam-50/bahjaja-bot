from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import os

TOKEN = os.getenv("BOT_TOKEN")

SUPPORT_GROUP = "https://t.me/bahjajastore"

USER_LANGUAGE = {}

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🌐 الموقع", url="https://bahjaja.wuiltstore.com/")],
        [InlineKeyboardButton("📝 تقديم شكوى", url="https://forms.gle/Rk388FAJRhgWRW6r7")],
        [InlineKeyboardButton("📱 تنزيل التطبيق", url="https://apkpure.com/ar/bahjaja-store/co.median.android.krxwerj")],
        [InlineKeyboardButton("💬 التواصل معنا", callback_data="contact")]
    ]

    await update.message.reply_text(
        "مرحباً بك 👋\n\nاختر الخدمة المطلوبة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# BUTTONS
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "contact":

        keyboard = [
            [InlineKeyboardButton("🇸🇦 العربية", callback_data="ar")],
            [InlineKeyboardButton("🇬🇧 English", callback_data="en")]
        ]

        await query.message.reply_text(
            "اختر اللغة:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "ar":

        USER_LANGUAGE[query.from_user.id] = "ar"

        await query.message.reply_text("تم اختيار العربية ✅\nاكتب رسالتك الآن.")

    elif query.data == "en":

        USER_LANGUAGE[query.from_user.id] = "en"

        await query.message.reply_text("English selected ✅\nSend your message.")

    elif query.data == "human":

        await query.message.reply_text(
            f"🚨 تم تحويلك للدعم\n{SUPPORT_GROUP}"
        )


# CHAT
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id
    language = USER_LANGUAGE.get(user_id, "ar")
    text = update.message.text

    if language == "ar":
        await update.message.reply_text(
            f"استلمنا رسالتك:\n\n{text}\n\n"
            "سيتم إضافة الذكاء الاصطناعي قريباً.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("👨‍💼 التحدث مع موظف", callback_data="human")]
            ])
        )
    else:
        await update.message.reply_text(
            f"Message received:\n\n{text}\n\n"
            "AI will be added soon.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("👨‍💼 Human Agent", callback_data="human")]
            ])
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
