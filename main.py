import datetime, random, logging
from telegram.ext import Application, MessageHandler, CommandHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR
)

logger = logging.getLogger(__name__)

jokes = ['Знатокам японской кухни. Интересно, поймёт ли японец выражение "одна шестая часть суши"',
         'Москва. Вывеска над дверью в офис-подвал: "Ремонтное предприятие "Металлик". Ремонт металлоизделий,'
         ' бытовой техники и так далее. "Мы ремонтируем всё!" Чуть ниже приписано от руки: '
         '"Стучите громче. Звонок не работает"',
         'Если во время празднования Нового года дело дошло до торта — праздник не удался!',
         'Объявление в газете: "Куплю оверлок. Хоть узнаю, что это"',
         'На весь мир прославились англичане чопорностью и пуританством. Даже в постели их поведение строго '
         'регламентировано этикетом. Например, джентльмен обязательно должен лежать слева от леди. И только в том '
         'случае, если они незнакомы, — справа',
         'Если чужая женщина нравится мужчине больше, чем своя, — значит, он в обеих чего-то недоглядел!',
         'Если вы хотите всегда быть в хорошем настроении, научитесь радоваться мелочам, скажем, зарплате. Мелочь, '
         'а приятно',
         'Американец думает на ходу, немец — стоя, англичанин — сидя, а русский — потом. Сначала делает, а потом '
         'думает, как бы расхлебать то, что наделал',
         'Только русский человек, если ему разрешить делать всё что угодно, не будет делать вообще ничего',
         'Лично для меня не так страшен приход конца света, как потеря конца скотча']


async def help(update, context):
    await update.message.reply_text("Доступные команды:\n/start - Запуск бота\n/help - Список команд\n/time - "
                                    "Текущее время\n/joke - Случайная шутка")


async def time(update, context):
    await update.message.reply_text(str(datetime.datetime.now().time()))


async def joke(update, context):
    await update.message.reply_text(random.choice(jokes))


def main():
    application = Application.builder().token('7366402891:AAEbEPstXAfP-NdaVuQrL6VBaF2IugxQ1b0').build()
    application.add_handlers([CommandHandler("help", help),
                              CommandHandler("time", time),
                              CommandHandler("joke", joke)])
    application.run_polling()


if __name__ == "__main__":
    main()
