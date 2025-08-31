from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


BOT_TOKEN = "8142399641:AAGZXXPwA5dSkxIRRhgBPuLtEqZ9N2Xwluw"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = (
        "Your gateway to the fastest-growing student-led community 🚀\n\n"
        "Glad to have you here!\n\n"
        "📸 <a href='https://instagram.com/nexus.ofnerds'>Follow us on Instagram</a>\n"
        "🚀 <a href='https://t.me/your_group_link'>Join Our Community</a>\n"
        "📢 <a href='https://t.me/your_channel_link'>Join Our Channel</a>"
    )

    await update.message.reply_text(
        message_text,
        parse_mode="HTML"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
