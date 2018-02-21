import logging
from queue import Queue
from threading import Thread
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Updater, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '504179513:AAEJT5PbCxOXwRJOjgHrTAAc9n4fQ54Tl-A'


def start(bot, update):
    update.message.reply_text('welcome MESSAGE')


def help(bot, update):
    update.message.reply_text('help message')


def echo(bot, update):
    update.message.reply_text('Привет! :hand: /n Я - бот Волонтёр Приморья! Я могу ответить на простые вопросы, связанные с волонтёрством!
'/nЯ ещё молодой и начинающий бот и многого не умею, но дай мне время, и я научусь делать новые вещи :blush:
'/nНабери одну из команд, чтобы получить ответ на интересующий тебя вопрос:
'/n/Book - расскажу тебе, как получить книжку волонтёра
'/n/Events - расскажу, на какие мероприятия ты можешь подать заявку в качестве волонтёра
'/n/Cat - пришлю тебе смешного кота!
'/nВ будущем я научусь делать и другие полезные штуки :smirk:
'/nНе спускай с меня глаз! :eyes:')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def book(bot, update):
    update.message.reply_text('Получи её у меня!')

def events(bot, update):
    update.message.reply_text('Сейчас у нас проходят такие мероприятия!')

def cat(bot, update):
    update.message.reply_sticker('CAADAgADnwADwl3uDLGxK0dMZWzwAg')

# Write your handlers here


def setup(webhook_url=None):
    """If webhook_url is not passed, run with long-polling."""
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:
        updater = Updater(TOKEN)
        bot = updater.bot
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("book", book))
        dp.add_handler(CommandHandler("events", events))
        dp.add_handler(CommandHandler("cat", cat))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)
    # Add your handlers here
    if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:
        bot.set_webhook()  # Delete webhook
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    setup()
