import telebot
from telebot import types
import kurs
import pogoda

bot = telebot.TeleBot('1080075133:AAHWlxmVVK3nUbf8dNrWO1O4ZaaRA1L42TY')

keyboard1 = types.ReplyKeyboardMarkup(True, True)
# keyboard1.row()
button1 = types.KeyboardButton("Курс")
button2 = types.KeyboardButton("Погода")

keyboard1.add(button1, button2)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здоровенькі були', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def txt(message):
    if message.chat.type == 'private':
        if message.text == "Курс":
            infoUa = kurs.getCurse()
            bot.send_message(message.chat.id,
                             str("Western Union Ukraine:\n" + infoUa[0] + '\n' + infoUa[1] + '\n' + infoUa[2]))
            infoPl = kurs.getCursePln()
            bot.send_message(message.chat.id,
                             str("Lodz kantor Poland:\n" + infoPl[0] + '\n' + infoPl[1] + '\n' + infoPl[2]))
        elif message.text == "Погода":
            info = pogoda.getPogoda()
            print(info)
            bot.send_message(message.chat.id, str("Погода Лодзь :\n"
                                                  + info[0][0] + "  -  Температура: " + info[1][0] + " Тиск: " +
                                                  info[2][0] + '\n'
                                                  + info[0][1] + "  -  Температура: " + info[1][1] + " Тиск: " +
                                                  info[2][1] + '\n'
                                                  + info[0][2] + "  -  Температура: " + info[1][2] + " Тиск: " +
                                                  info[2][2] + '\n'
                                                  + info[0][3] + "  -  Температура: " + info[1][3] + " Тиск: " +
                                                  info[2][3] + '\n'
                                                  + info[0][4] + "  -  Температура: " + info[1][4] + " Тиск: " +
                                                  info[2][4] + '\n'
                                                  + info[0][5] + "  -  Температура: " + info[1][5] + " Тиск: " +
                                                  info[2][5] + '\n'
                                                  + info[0][6] + "  -  Температура: " + info[1][6] + " Тиск: " +
                                                  info[2][6] + '\n'
                                                  + info[0][7] + "  -  Температура: " + info[1][7] + " Тиск: " +
                                                  info[2][7] + '\n'
                                                  ))


bot.polling(none_stop=True)
