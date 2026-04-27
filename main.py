import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем бота
# TOKEN заменить на свой
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


# ===================== КОМАНДА /start =====================

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)  # вывод в консоль (для проверки)
    bot.reply_to(
        message,
        "Привет! 🌍\n"
        "Я эко-бот.\n"
        "Помогаю узнать, как правильно сортировать отходы."
    )

    # создаем клавиатуру (кнопки под сообщением)
    keyboard = InlineKeyboardMarkup()

    # создаем кнопки
    btn1 = InlineKeyboardButton("♻️ Пластик", callback_data="plastic")
    btn2 = InlineKeyboardButton("📄 Бумага", callback_data="paper")
    btn3 = InlineKeyboardButton("🍾 Стекло", callback_data="glass")

    # добавляем кнопки в клавиатуру
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)

    # отправляем сообщение с кнопками
    bot.send_message(
        message.chat.id,
        "Выбери тип отходов:",
        reply_markup=keyboard
    )


# ===================== ОБРАБОТКА НАЖАТИЯ КНОПОК =====================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    # подтверждаем нажатие кнопки (убираем "часики")
    bot.answer_callback_query(call.id)

    # если нажали кнопку Пластик
    if call.data == "plastic":

        bot.send_message(
            call.message.chat.id,
            "♻️ Пластик:\n\n"
            "1️⃣ Ополосни упаковку.\n"
            "2️⃣ Сними крышку.\n"
            "3️⃣ Сожми бутылку.\n"
            "4️⃣ Выброси в контейнер для пластика."
        )

    # если нажали кнопку Бумага
    elif call.data == "paper":

        bot.send_message(
            call.message.chat.id,
            "📄 Бумага:\n\n"
            "1️⃣ Убедись, что она сухая.\n"
            "2️⃣ Убери пластиковые элементы.\n"
            "3️⃣ Выброси в контейнер для макулатуры."
        )

    # если нажали кнопку Стекло
    elif call.data == "glass":

        bot.send_message(
            call.message.chat.id,
            "🍾 Стекло:\n\n"
            "1️⃣ Промой бутылку.\n"
            "2️⃣ Сними крышку.\n"
            "3️⃣ Выброси в контейнер для стекла."
        )


# ===================== КОМАНДА /eco =====================

@bot.message_handler(commands=['eco'])
def eco_tips(message):

    bot.reply_to(
        message,
        "🌱 Эко-советы:\n\n"
        "• Используй многоразовые сумки\n"
        "• Экономь воду\n"
        "• Выключай свет\n"
        "• Сортируй отходы"
    )


print("Эко-бот в действии 🌍")
bot.polling()