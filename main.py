import telebot
from bot_logic import gen_pass, flip_coin, gen_emoji, random_answer  # Импортируем функции из bot_logic
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7641936499:AAFl_Z3lyBcXHWAMUvTO4PFJRJPC1LkxsmI")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Длина пароля 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emoji'])
def send_emoji(message):
    emoji = gen_emoji()
    bot.reply_to(message, f"Вот эмоджи': {emoji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['predict'])
def send_predict(message):
    answer = random_answer()
    bot.reply_to(message, f"Мой ответ: {answer}")

# Запускаем бота
bot.polling()
