import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "ТОКЕН_ОТ_BOTFATHER"
ADMIN_ID = 123456789  # свой Telegram ID

logging.basicConfig(level=logging.INFO)

async def channel_post_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        channel = update.channel_post.chat.username
        message_id = update.channel_post.message_id
        if channel:
            link = f"https://t.me/{channel}/{message_id}"
            await context.bot.send_message(chat_id=ADMIN_ID, text=link)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, channel_post_handler))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
