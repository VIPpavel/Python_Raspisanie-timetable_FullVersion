import telebot
import config
import pandas as pd
import datetime

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("расписание на сегодня")
    item2 = telebot.types.KeyboardButton("расписание на завтра")

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
            b = datetime.datetime.today().strftime('%A')
            cols = []
            if b == 'Sunday' or 'Monday' or 'Saturday':
                cols = [1]
            elif b == 'Monday':
                cols = [1]
            elif b == 'Tuesday':
                cols = [2]
            elif b == 'Wednesday':
                cols = [3]
            elif b == 'Thursday':
                cols = [4]
            elif b == 'Friday':
                cols = [5]
            print(cols)
            top = pd.read_excel('raspis.xlsx', nrows=7, usecols=cols)
            a = top.values.tolist()
            c = []
            for i in range(len(a)):
                for j in range(len(a[i])):
                    c.append(a[i][j])
                c.append("\n")
                print(c)
                h = ''.join(c)
            bot.send_message(message.chat.id, b +'\n' + h)

        elif message.text == "расписание на завтра":
            b = datetime.datetime.today().strftime('%A')
            cols = []
            if b == 'Sunday' or 'Saturday':
                cols = [1]
            elif b == 'Monday':
                cols = [2]
            elif b == 'Tuesday':
                cols = [3]
            elif b == 'Wednesday':
                cols = [4]
            elif b == 'Thursday':
                cols = [5]
            elif b == 'Friday':
                cols = [1]
            top = pd.read_excel('raspis.xlsx', nrows=7, usecols=cols)
            a = top.values.tolist()
            c = []
            for i in range(len(a)):
                for j in range(len(a[i])):
                    c.append(a[i][j])
                c.append("\n")
                v = ''.join(c)
            bot.send_message(message.chat.id, b + '\n' + v)


bot.polling(none_stop=True)
