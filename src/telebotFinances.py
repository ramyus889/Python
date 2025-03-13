import telebot
import json
from datetime import datetime

# Токен вашего Telegram-бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Словарь для хранения данных о финансах
finances = {
    'income': [],  # Список доходов: (сумма, описание, дата)
    'expenses': []  # Список расходов: (сумма, описание, дата)
}

# Файл для сохранения данных
DATA_FILE = 'finances.json'

# Загрузка данных из файла при старте


def load_data():
    global finances
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            finances = json.load(f)
    except FileNotFoundError:
        save_data()  # Создаём пустой файл, если его нет

# Сохранение данных в файл


def save_data():
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(finances, f, ensure_ascii=False, indent=2)

# Функция для разбора суммы и описания


def parse_amount_and_desc(text):
    parts = text.split(maxsplit=1)  # Разделяем на 2 части
    try:
        amount = float(parts[0])  # Первая часть — число
        description = parts[1]
        return amount, description
    except ValueError:
        try:
            amount = float(parts[1])  # Вторая часть — число
            description = parts[0]
            return amount, description
        except (ValueError, IndexError):
            return None, None

# Обработка всех текстовых сообщений


@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text.strip()
    command_parts = text.split(maxsplit=1)
    command = command_parts[0].lower()  # Первое слово — команда

    # Команда "start"
    if command == 'start':
        bot.reply_to(message, "Привет! Это бот для управления финансами.\n"
                              "Доступные команды:\n"
                              "доход <сумма> <описание> — добавить доход\n"
                              "расход <сумма> <описание> — добавить расход\n"
                              "итог — показать итоги\n"
                              "сброс — сбросить все данные\n"
                              "Порядок суммы и описания не важен!")
        return

    # Команда "доход"
    if command == 'доход':
        if len(command_parts) < 2:
            bot.reply_to(
                message, "Формат: доход <сумма> <описание>\nПример: доход 5000 Зарплата")
            return

        amount, description = parse_amount_and_desc(command_parts[1])
        if amount is None:
            bot.reply_to(
                message, "Укажите сумму и описание правильно!\nПример: доход 5000 Зарплата или доход Зарплата 5000")
            return

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        finances['income'].append((amount, description, date))
        save_data()
        bot.reply_to(message, f"Доход {amount} ({description}) добавлен!")
        return

    # Команда "расход"
    if command == 'расход':
        if len(command_parts) < 2:
            bot.reply_to(
                message, "Формат: расход <сумма> <описание>\nПример: расход 1000 Еда")
            return

        amount, description = parse_amount_and_desc(command_parts[1])
        if amount is None:
            bot.reply_to(
                message, "Укажите сумму и описание правильно!\nПример: расход 1000 Еда или расход Еда 1000")
            return

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        finances['expenses'].append((amount, description, date))
        save_data()
        bot.reply_to(message, f"Расход {amount} ({description}) добавлен!")
        return

    # Команда "итог"
    if command == 'итог':
        total_income = sum(item[0] for item in finances['income'])
        total_expenses = sum(item[0] for item in finances['expenses'])
        balance = total_income - total_expenses

        summary_text = (
            f"📊 Итог финансов:\n"
            f"Доходы: {total_income:.2f}\n"
            f"Расходы: {total_expenses:.2f}\n"
            f"Баланс: {balance:.2f}"
        )

        if finances['income']:
            summary_text += "\n\n📈 Доходы:"
            for amount, desc, date in finances['income']:
                summary_text += f"\n- {amount:.2f} ({desc}) — {date}"

        if finances['expenses']:
            summary_text += "\n\n📉 Расходы:"
            for amount, desc, date in finances['expenses']:
                summary_text += f"\n- {amount:.2f} ({desc}) — {date}"

        bot.reply_to(
            message, summary_text if finances['income'] or finances['expenses'] else "Пока нет данных.")
        return

    # Команда "сброс"
    if command == 'сброс':
        global finances
        finances = {'income': [], 'expenses': []}  # Очищаем данные
        save_data()  # Сохраняем пустой словарь в файл
        bot.reply_to(message, "Все данные сброшены. Можно начинать заново!")
        return

    # Если команда не распознана
    bot.reply_to(
        message, "Неизвестная команда. Напишите 'start' для списка команд.")


# Загружаем данные при запуске
load_data()

# Запуск бота
bot.polling(none_stop=True)
