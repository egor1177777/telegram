from telegram.ext import Application, MessageHandler, CommandHandler, filters


async def start(update, context):
    await update.message.reply_text("Привет! Я эхо-бот.")


async def echo(update, context):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token('7366402891:AAEbEPstXAfP-NdaVuQrL6VBaF2IugxQ1b0').build()
    text_handler = MessageHandler(filters.TEXT, echo)
    command_handler = CommandHandler("start", start)
    application.add_handler(command_handler)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
