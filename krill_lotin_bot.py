from transliterate import to_cyrillic, to_latin
import telebot
bot = telebot.TeleBot('8385006554:AAHbRATPI5tA-NHaASOOAq77cCFr66ebRkQ', parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, hush kelibsiz"
                               "\n matn kiriting:")

@bot.message_handler(func=lambda message: True)
def eco_all(message):
    msg=message.text
    javob=to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob)
bot.polling()