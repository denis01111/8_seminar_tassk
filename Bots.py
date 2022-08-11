from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


bot = Bot(token='5455540322:AAFSyeSpqCKuiGvskoyJVE-AR8jCb-QP4po')
updater = Updater(token='5455540322:AAFSyeSpqCKuiGvskoyJVE-AR8jCb-QP4po')
dispatcher = updater.dispatcher

START = 0
NUMBERFIRST = 1
NUMBERSECOND = 2
OPERATION = 3
numberOne = ''
numberTwo = ''
oper = ''


def numbers(number):
    pass


def result(x, y, z):
    pass


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, который умеет '
                                                       'считать комплексные и рациональные числа! Напиши 2 числа\n'
                                                       'Введи первое число: ')

    return NUMBERFIRST


def numberFirst(update, context):
    global numberOne
    numberOne = numbers(update.message.text)
    context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведи второе число: ')

    return NUMBERSECOND


def numberSecond(update, context):
    global numberTwo
    numberTwo = numbers(update.message.text)
    context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведи операцию (+, -, *, /): ')

    return OPERATION


def operation(update, context):
    global oper

    context.bot.send_message(update.effective_chat.id, f'Результат: {result(numberOne, numberTwo, update.message.text)}')

    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
numone_handler = MessageHandler(Filters.text, numberFirst)
numtwo_handler = MessageHandler(Filters.text, numberSecond)
oper_handler = MessageHandler(Filters.text, operation)
conv_handler = ConversationHandler(fallbacks=[start_handler],
                                   states={
                                       NUMBERFIRST: [numone_handler],
                                       NUMBERSECOND: [numtwo_handler],
                                       OPERATION: [oper_handler]
                                   },
                                   entry_points=[cancel_handler])



updater.start_polling()
updater.idle()