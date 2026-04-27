import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")

bot = telebot.TeleBot(TOKEN)

# ===================== /start =====================

@bot.message_handler(commands=['start'])
def send_welcome(message):

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton("♻️ Пластик", callback_data="plastic"),
        InlineKeyboardButton("📄 Бумага", callback_data="paper"),
        InlineKeyboardButton("🍾 Стекло", callback_data="glass")
    )

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

    chat_id = call.message.chat.id

    if call.data == "plastic":
        bot.send_message(chat_id,
            "♻️ Пластик:\n\n"
            "1️⃣ Ополосни упаковку.\n"
            "2️⃣ Сними крышку.\n"
            "3️⃣ Сожми бутылку.\n"
            "4️⃣ В контейнер для пластика."
        )

    elif call.data == "paper":
        bot.send_message(chat_id,
            "📄 Бумага:\n\n"
            "1️⃣ Убедись, что она сухая.\n"
            "2️⃣ Убери пластиковые элементы.\n"
            "3️⃣ В макулатуру."
        )

    elif call.data == "glass":
        bot.send_message(chat_id,
            "🍾 Стекло:\n\n"
            "1️⃣ Промой бутылку.\n"
            "2️⃣ Сними крышку.\n"
            "3️⃣ В контейнер стекла."
        )

# ===================== /eco =====================

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
bot.infinity_polling()
