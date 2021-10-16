import telebot
import config
import pandas as pd
import datetime

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("расписание на сегодня")
    item2 = telebot.types.KeyboardButton("расписание на неделю")

    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть твоим помощником.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler()
def lalala(message):
    # bot.send_message(message.chat.id, message.text)
    if message.chat.type == "private":
        if message.text == "расписание на сегодня":  # курс биткоина
            cols = [0, 2]
            top = pd.read_excel('raspis.xlsx', nrows=4, usecols=cols)
            a = top.values.tolist()
            b = datetime.datetime.today().strftime('%A')
            bot.send_message(message.chat.id, b)
            print(a)

            for i in range(len(a)):
                bot.send_message(message.chat.id, str(i + 1) + "-----------")
                for j in range(len(a[i])):
                    bot.send_message(message.chat.id, a[i][j])


        elif message.text == "расписание на неделю":
            cols = [0, 1]
            top = pd.read_excel('raspis.xlsx', nrows=4, usecols=cols)
            a = top.values.tolist()
            b = datetime.datetime.today().strftime('%A')

            print(a)
            print(b)
            for i in range(len(a)):
                for j in range(len(a[i])):
                    bot.send_message(message.chat.id, a[i][j])


bot.polling(none_stop=True)
