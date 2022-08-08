from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


bot = Bot(token='5455540322:AAFSyeSpqCKuiGvskoyJVE-AR8jCb-QP4po')
updater = Updater(token='5455540322:AAFSyeSpqCKuiGvskoyJVE-AR8jCb-QP4po')
dispatcher = updater.dispatcher

STATE0 = 1
STATE1 = 2
STATE2 = 3


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Напиши мне "Привет" и мы начнем болтать')

    return STATE0


def message0(update, context):
    if 'прив' in update.message.text.lower():
        context.bot.send_message(update.effective_chat.id, 'Привет!\nКак твои дела?')
        return STATE1
    else:
        context.bot.send_message(update.effective_chat.id, 'Я тебя не очень хорошо понял, напиши мне "Привет".')


def message1(update, context):
    if 'хор' in update.message.text.lower() or 'отл' in update.message.text.lower():
        context.bot.send_message(update.effective_chat.id, 'Отлично, я очень рад!')
    elif 'плох' in update.message.text.lower():
        context.bot.send_message(update.effective_chat.id, 'Не переживай все наладится, я в тебя верю!')

    context.bot.send_message(update.effective_chat.id, 'Чем сегодня занимаешься?')
    return STATE2


def message2(update, context):
    context.bot.send_message(update.effective_chat.id, 'Мне без разницы, спросил, чтобы протестировать бота!')
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Рад был пообщаться! Всего доброго!')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
message0_handler = MessageHandler(Filters.text, message0)
message1_handler = MessageHandler(Filters.text, message1)
message2_handler = MessageHandler(Filters.text, message2)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={STATE0: [message0_handler],
                                           STATE1: [message1_handler],
                                           STATE2: [message2_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(conv_handler)

# В конце |||
updater.start_polling()
updater.idle()  # ctrl + C