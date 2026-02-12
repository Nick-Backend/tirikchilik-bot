
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config.settings import settings



def get_main_menu():
    keyboard = [
       
        [KeyboardButton("🔥 Mahsulotlar", web_app=WebAppInfo(url="https://uzum.uz")), KeyboardButton("🛒 Savat")],
       
        ["🤝 Hamkorlik", "ℹ️ Ma'lumot"],
       
        ["🌐 Tilni tanlash"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
def get_language_menu():
    keyboard = [
        [InlineKeyboardButton("🇷🇺 Русский", callback_data='lang_ru')],
        [InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='lang_uz')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update, context):
    await update.message.reply_text(
        f"Assalomu Alaykum, {update.effective_user.first_name}!",
        reply_markup=get_main_menu()
    )

async def handle_language_callback(update, context):
    query = update.callback_query
    await query.answer() 

    if query.data == 'lang_uz':
        await query.message.reply_text("Siz O'zbek tilini tanladingiz 🇺🇿")
    elif query.data == 'lang_ru':
        await query.message.reply_text("Siz Rus tilini tanladingiz 🇷🇺")

async def handle_message(update, context):
    user_text = update.message.text

    if user_text == "🛒 Savat":
        await update.message.reply_text("Sizning savatingiz bo'sh 🛒")

    elif user_text == "🤝 Hamkorlik":
        await update.message.reply_text(
            "Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz...\nMenejer: @testbackgrountbot"
        )

    elif user_text == "ℹ️ Ma'lumot":
        info_keyboard = [
            ["✍️ Izoh qoldirish"],
            ["🚀 Yetkazib berish shartlari", "☎️ Kontaktlar"],
            ["🏠 Bosh menyu"]
        ]
        await update.message.reply_text("Kerakli bo'limni tanlang 👇", 
            reply_markup=ReplyKeyboardMarkup(info_keyboard, resize_keyboard=True))

    elif user_text == "🌐 Tilni tanlash":
        await update.message.reply_text("Iltimos, tilni tanlang:", reply_markup=get_language_menu())

    elif user_text == "🏠 Bosh menyu":
        await update.message.reply_text("Asosiy menyuga qaytdingiz.", reply_markup=get_main_menu())


def main():
   
    app = ApplicationBuilder().token(settings.TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
   
    app.add_handler(CallbackQueryHandler(handle_language_callback))

    print("ishladi")
    app.run_polling()

if __name__ == '__main__':
    main()