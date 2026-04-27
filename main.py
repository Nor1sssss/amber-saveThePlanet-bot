import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

# 👉 ВОТ СЮДА
if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")

# 👉 И только потом создаём бота
bot = telebot.TeleBot(TOKEN)
# ===================== КОМАНДА /start =====================

@bot.message_handler(commands=['start'])
def send_welcome(message):

    keyboard = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("♻️ Пластик", callback_data="plastic")
    btn2 = InlineKeyboardButton("📄 Бумага", callback_data="paper")
    btn3 = InlineKeyboardButton("🍾 Стекло", callback_data="glass")

    keyboard.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "Выбери тип отходов:",
        reply_markup=keyboard
    )

# ===================== CALLBACK =====================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    print("🔥 CALLBACK WORKS:", call.data)

    bot.answer_callback_query(call.id)

# ===================== ОБРАБОТКА НАЖАТИЯ КНОПОК =====================


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
