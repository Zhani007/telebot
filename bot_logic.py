import random
import os
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emoji():
    emoji = ["( OvO)", "(uwu)", "(Q-Q)", "(;o;)"]
    return random.choice(emoji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"

def random_answer():
    answers = [
        "Да",
        "Нет",
        "Возможно",
        "Вероятно",
        "Маловероятно",
        "Спроси позже",
        "Да, но будь осторожен",
        "Нет, и даже не думай",
        "Абсолютно точно!",
        "Даже не сомневайся"
    ]
    return random.choice(answers)

def memes():
    file_names = os.listdir('image')
    file_names = random.choice(file_names)
    return file_names

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


secret_numbers = {}  # Будет хранить загаданные числа {chat_id: число}
def start_game(chat_id):
    """Загадывает число от 1 до 10"""
    secret_numbers[chat_id] = random.randint(1, 10)
    return "Я загадал число от 1 до 10. Попробуй угадать!"


def check_guess(chat_id, user_guess):
    """Проверяет догадку пользователя"""
    if chat_id not in secret_numbers:
        return "Сначала начни игру командой /start_game"

    secret = secret_numbers[chat_id]

    if user_guess == secret:
        del secret_numbers[chat_id]  # Удаляем завершённую игру
        return "🎉 Угадал!"
    elif user_guess < secret:
        return "⬆️ Больше"
    else:
        return "⬇️ Меньше"

moods_db = {}  # {chat_id: [список настроений]}
def save_mood(chat_id, mood):
    """Сохраняет настроение"""
    if chat_id not in moods_db:
        moods_db[chat_id] = []
    moods_db[chat_id].append(mood)
    return f"Запомнил: {mood}"

def get_moods(chat_id):
    """Показывает все настроения"""
    if chat_id not in moods_db or not moods_db[chat_id]:
        return "Ты ещё не записывал(а) настроение"
    return "Все твои настроения:\n" + "\n".join(moods_db[chat_id])
