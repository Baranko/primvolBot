import logging
from queue import Queue
from threading import Thread
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '504179513:AAEJT5PbCxOXwRJOjgHrTAAc9n4fQ54Tl-A'



def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def start(bot, update):
    button_list = [
    InlineKeyboardButton("Мероприятия",callback_data="events"),
    InlineKeyboardButton("Стикеры",callback_data="cat"),
    InlineKeyboardButton("Волонтёрская книжка",callback_data="book")
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(update.message.chat.id, "Выберите интересующий вас раздел:", reply_markup=reply_markup)
    return FIRST

def echo(bot, update):
    button_list = [
    InlineKeyboardButton("Мероприятия",callback_data="events"),
    InlineKeyboardButton("Стикеры",callback_data="cat"),
    InlineKeyboardButton("Волонтёрская книжка",callback_data="book")
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(update.message.chat.id, "Выберите интересующий вас раздел:", reply_markup=reply_markup)
    return FIRST
    
def book(bot, update):
    query = update.callback_query
    if query.data == "book":
        button_list = [
        InlineKeyboardButton("Нет",callback_data="no"),
        InlineKeyboardButton("Да",callback_data="yes"),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        bot.sendMessage(
            chat_id=query.message.chat_id,
            parse_mode = "HTML",
            text="<b>Волонтёрская книжка:</b> \U0001F4D4 \r\n" +
            "Волонтёрская книжка - документ, фиксирующий все достижения волонтёра в его деятельности: в каких мероприятиях он принимал участие и сколько времени у него это заняло \r\n " 
            +"Чтобы получить волонтёрскую книжку, необходимо выполнить следующие действия:  \U0001F4DD \r\n"
            +u'1. Скачать заявление у <b>меня</b> или из группы "Волонтер Приморья" в сети <b>Вконтакте</b>! \r\n'
            +'2. <b>Распечатать и заполнить</b> скачанное заявление! \U0000270F \r\n'
            +'3. Прикрепить к заявлению <b>две</b> фотографии формата <b>3x4</b>! \U0001F466\U0001F467 \r\n'
            +'4. Принести заявление с фотографиями по адресу <b>г. Владивосток, ул. Алеутская 45а, каб. 432</b>! \U0001F3E2 \r\n'
            +'5. Или отдать заявление своему <b>координатору волонтёров</b> на мероприятии!\r\n '
            +'<b>Вы желаете скачать заявление?</b>'	, reply_markup=reply_markup
        )
    elif query.data == "events":
        query4 = update.callback_query
        bot.sendPhoto(query4.message.chat_id, "AgADAgAD76gxGwgqqUmkrr-Je_lBDr_KRg4ABHLG5rU3aTi8-IgAAgI")
        bot.sendMessage(
            chat_id=query4.message.chat_id,
            parse_mode = "HTML",
            text="<b>Каникулы с пользой</b>"
            +"С 26 по 29 марта в городе Владивостоке при поддержке благотворительного фона <b>«ВладМама»</b> пройдет краевая профориентационная смена <b>«Каникулы с пользой»</b> для воспитанников детских домов, школ-интернатов Приморского края в возрасте от 13 до 17 лет \r\n"
            + "Основная функция будет заключаться в <b>сопровождении  и общении с детьми</b> \r\n"
            + "Помощь понадобиться 27 марта с 18:00 до 21:00 и 28 марта с 9:30 до 13:00. Одно из требований организаторов к волонтерам - это <b>возраст от 18 лет</b> \r\n"
            + "Если у вас есть желание и возможность помочь, то ждем вашей заявки по ссылке https://goo.gl/forms/Q9gKYaBl24utTrOq1  до 15:00 26 марта \r\n"
            + "Хочешь получить невероятные эмоции от общения с ребятами, а так же новые удивительные  знакомства и опыт наставничества? \r\n"
            + "Тогда подавай заявку, мы тебя ждем!"
        )
        button_list = [
        InlineKeyboardButton("Мероприятия",callback_data="events"),
        InlineKeyboardButton("Стикеры",callback_data="cat"),
        InlineKeyboardButton("Волонтёрская книжка",callback_data="book")
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        bot.send_message(query4.message.chat_id, "Выберите интересующий вас раздел:", reply_markup=reply_markup)
    elif query.data == "no":
        query1 = update.callback_query
        button_list = [
        InlineKeyboardButton("Мероприятия",callback_data="events"),
        InlineKeyboardButton("Стикеры",callback_data="cat"),
        InlineKeyboardButton("Волонтёрская книжка",callback_data="book")
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        bot.send_message(query1.message.chat_id, "Выберите интересующий вас раздел:", reply_markup=reply_markup)
    elif query.data == "cat":
        query3 = update.callback_query
        bot.sendSticker(query3.message.chat_id, 'CAADAgADnwADwl3uDLGxK0dMZWzwAg')
        button_list = [
        InlineKeyboardButton("Мероприятия",callback_data="events"),
        InlineKeyboardButton("Стикеры",callback_data="cat"),
        InlineKeyboardButton("Волонтёрская книжка",callback_data="book")
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        bot.send_message(query3.message.chat_id, "Выберите интересующий вас раздел:", reply_markup=reply_markup)
    else:
        query2 = update.callback_query
        bot.sendDocument(query2.message.chat_id, "BQADAgADjwEAAggqqUnI-vhNr1yXSgI")
        button_list = [
        InlineKeyboardButton("Мероприятия",callback_data="events"),
        InlineKeyboardButton("Стикеры",callback_data="cat"),
        InlineKeyboardButton("Волонтёрская книжка",callback_data="book")
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        bot.send_message(query2.message.chat_id, "Выберите интересующий вас раздел:", reply_markup=reply_markup)


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
    
        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(CallbackQueryHandler(book))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
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
