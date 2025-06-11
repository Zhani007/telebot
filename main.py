import telebot
from bot_logic import gen_pass, flip_coin, gen_emoji, random_answer, memes, get_duck_image_url, check_guess, start_game, save_mood, get_moods #Импортируем функции из bot_logic
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("TOCKEN")

def get_help_message():
    """Возвращает форматированное сообщение со списком всех команд"""
    return """
📚 <b>Список всех команд бота:</b>

<b>Основные команды:</b>
/start - Начать работу с ботом
/hello - Получить приветствие
/bye - Попрощаться с ботом
/help - Показать это справочное сообщение

<b>Генераторы:</b>
/pass - Сгенерировать случайный пароль (10 символов)
/emoji - Получить случайный эмодзи
/coin - Подбросить монетку
/predict - Получить случайный ответ на вопрос (типа магического шара)
/mem - Получить случайный мем
/duck - Получить случайное изображение утки

<b>Игры:</b>
/start_game - Начать игру "Угадай число" (от 1 до 10)
(после начала игры просто присылайте числа)

<b>Дневник настроения:</b>
/mood - Записать своё настроение
/my_moods - Показать все ваши сохранённые настроения
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start"""
    help_text = "Привет! Я Fluffy Cat! Твой пушистый котик. Вот что я умею:\n" + get_help_message()
    bot.reply_to(message, help_text, parse_mode='HTML')

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

@bot.message_handler(commands=['mem'])
def send_mem(message):
    file_name = memes()
    with open(f'image/{file_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['start_game'])
def start_number_game(message):
    reply = start_game(message.chat.id)
    bot.reply_to(message, reply)

@bot.message_handler(func=lambda m: m.text.isdigit())
def handle_guess(message):
    try:
        guess = int(message.text)
        reply = check_guess(message.chat.id, guess)
        bot.reply_to(message, reply)
    except ValueError:
        pass

@bot.message_handler(commands=['mood'])
def ask_mood(message):
    text = "Какое у тебя настроение? Напиши одним словом (например: Радость, Грусть)"
    bot.reply_to(message, text)

@bot.message_handler(func=lambda m: len(m.text.split()) == 1 and not m.text.startswith('/'))
def save_user_mood(message):
    reply = save_mood(message.chat.id, message.text)
    bot.reply_to(message, reply)

@bot.message_handler(commands=['my_moods'])
def show_moods(message):
    reply = get_moods(message.chat.id)
    bot.reply_to(message, reply)
# Запускаем бота
bot.polling(
