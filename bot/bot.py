import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import random

bot = telebot.TeleBot('7859744906:AAE0gXLmXtONHpslxcpnhOXqK42kerU9dAA')
favorite_recipes = {}
recipes = {
    "Яблочный пирог":
        "Ингредиенты:\n"
        "- 2 стакана муки\n- 200 г сливочного масла\n- 1 стакан сахара\n"
        "- 4 яблока\n- 1 ч.л. корицы\n\n"
        "Приготовление:\n"
        "1. Замесите тесто из муки, масла и половины сахара\n"
        "2. Яблоки нарежьте дольками, смешайте с оставшимся сахаром и корицей\n"
        "3. Выложите тесто в форму, сверху яблоки\n"
        "4. Выпекайте 40 минут при 180°C",
    "Шоколадный кекс":
        "Ингредиенты:\n"
        "- 1.5 стакана муки\n- 1 стакан сахара\n- 100 г какао\n"
        "- 1 ч.л. соды\n- 100 мл растительного масла\n- 250 мл воды\n\n"
        "Приготовление:\n"
        "1. Смешайте все сухие ингредиенты\n"
        "2. Добавьте масло и воду, перемешайте\n"
        "3. Вылейте тесто в форму\n"
        "4. Выпекайте 30 минут при 180°C",
    "Овсяное печенье":
        "Ингредиенты:\n"
        "- 1 стакан овсяных хлопьев\n- 0.5 стакана муки\n"
        "- 100 г сливочного масла\n- 0.5 стакана сахара\n- 1 яйцо\n\n"
        "Приготовление:\n"
        "1. Растопите масло, смешайте с сахаром и яйцом\n"
        "2. Добавьте хлопья и муку\n"
        "3. Сформируйте печенье ложкой\n"
        "4. Выпекайте 15 минут при 190°C",
    "Банановый хлеб":
        "Ингредиенты:\n"
        "- 3 спелых банана\n- 2 стакана муки\n- 1 стакан сахара\n"
        "- 1 ч.л. соды\n- 2 яйца\n- 100 г сливочного масла\n\n"
        "Приготовление:\n"
        "1. Разомните бананы вилкой\n"
        "2. Смешайте все ингредиенты\n"
        "3. Вылейте тесто в форму\n"
        "4. Выпекайте 50 минут при 170°C",
    "Сырники":
        "Ингредиенты:\n"
        "- 500 г творога\n- 2 яйца\n- 3 ст.л. сахара\n"
        "- 5 ст.л. муки\n- щепотка соли\n\n"
        "Приготовление:\n"
        "1. Смешайте творог с яйцами и сахаром\n"
        "2. Добавьте муку и соль\n"
        "3. Сформируйте сырники\n"
        "4. Жарьте на среднем огне 3-4 минуты с каждой стороны",
    "Блины":
        "Ингредиенты:\n"
        "- 2 стакана молока\n- 2 яйца\n- 1.5 стакана муки\n"
        "- 2 ст.л. сахара\n- щепотка соли\n- 2 ст.л. растительного масла\n\n"
        "Приготовление:\n"
        "1. Взбейте яйца с сахаром и солью\n"
        "2. Добавьте молоко и муку, перемешайте\n"
        "3. Добавьте масло\n"
        "4. Жарьте на хорошо разогретой сковороде",
    "Пирожки с капустой":
        "Ингредиенты:\n"
        "- 500 г дрожжевого теста\n- 300 г тушеной капусты\n"
        "- 1 луковица\n- 1 яйцо для смазки\n\n"
        "Приготовление:\n"
        "1. Обжарьте лук, смешайте с капустой\n"
        "2. Раскатайте тесто, нарежьте на кружки\n"
        "3. Наполните начинкой, защипните края\n"
        "4. Смажьте яйцом, выпекайте 20 минут при 200°C",
    "Чизкейк":
        "Ингредиенты:\n"
        "- 200 г печенья\n- 100 г сливочного масла\n- 500 г творожного сыра\n"
        "- 150 г сахара\n- 3 яйца\n- 200 мл сливок\n\n"
        "Приготовление:\n"
        "1. Измельчите печенье, смешайте с растопленным маслом - это основа\n"
        "2. Взбейте сыр с сахаром, добавьте яйца и сливки\n"
        "3. Выложите на основу\n"
        "4. Выпекайте 1 час при 160°C в духовке с водяной баней"
}
baking_tips = [
    "🔸 Все ингредиенты должны быть комнатной температуры",
    "🔸 Муку всегда просеивайте для воздушности выпечки",
    "🔸 Духовку разогревайте заранее",
    "🔸 Не открывайте духовку первые 15-20 минут выпекания",
    "🔸 Проверяйте готовность деревянной зубочисткой",
    "🔸 Дайте выпечке немного остыть в форме перед подачей",
    "🔸 Для пышности добавляйте щепотку соли в тесто",
    "🔸 Смазывайте форму маслом и присыпайте мукой"
]
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.row("🔀 Случайный рецепт", "🔍 Поиск по ингредиентам")
    keyboard.row("📜 Все рецепты", "💡 Советы по выпечке")
    keyboard.row("⏱️ Время приготовления", "❤️ Любимые рецепты")
    keyboard.row("🆘 Помощь")
    return keyboard

def create_favorites_keyboard(user_id):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if str(user_id) in favorite_recipes and favorite_recipes[str(user_id)]:
        keyboard.add("❌ Удалить любимый рецепт")
    keyboard.add("➕ Добавить рецепт в избранное")
    keyboard.add("🔙 Назад в меню")
    return keyboard

def create_remove_favorites_keyboard(user_id):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if str(user_id) in favorite_recipes and favorite_recipes[str(user_id)]:
        for recipe in favorite_recipes[str(user_id)]:
            keyboard.add(f"❌ {recipe}")
    keyboard.add("🔙 Назад к избранному")
    return keyboard

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот с рецептами выпечки. Выбери действие:",
        reply_markup=create_main_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "🔀 Случайный рецепт")
def random_recipe(message):
    recipe = random.choice(list(recipes.keys()))
    bot.send_message(message.chat.id, f"Случайный рецепт: {recipe}\n\n{recipes[recipe]}")

@bot.message_handler(func=lambda message: message.text == "🔍 Поиск по ингредиентам")
def search_by_ingredient(message):
    msg = bot.send_message(message.chat.id, "Введите ингредиент для поиска:", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, process_ingredient_search)
def process_ingredient_search(message):
    ingredient = message.text.lower()
    found_recipes = []

    for recipe_name, recipe_text in recipes.items():
        if ingredient in recipe_text.lower():
            found_recipes.append(recipe_name)

    if found_recipes:
        response = "Найдены рецепты:\n\n" + "\n".join(found_recipes)
    else:
        response = "Рецепты с таким ингредиентом не найдены."

    bot.send_message(message.chat.id, response, reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda message: message.text == "📜 Все рецепты")
def show_all_recipes(message):
    response = "🍰 <b>Все доступные рецепты:</b>\n\n" + "\n".join([f"• {name}" for name in recipes.keys()])
    bot.send_message(message.chat.id, response, parse_mode='HTML')
    msg = bot.send_message(message.chat.id,
                           "Введите название рецепта, чтобы увидеть его полное описание:",
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, show_full_recipe)
def show_full_recipe(message):
    recipe_name = message.text
    if recipe_name in recipes:
        recipe_text = recipes[recipe_name].replace('\n\n', '\n')
        response = f"<b>{recipe_name}</b>\n\n{recipe_text}"
        bot.send_message(message.chat.id, response, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "Рецепт с таким названием не найден.")

    bot.send_message(message.chat.id, "Возвращаемся в главное меню:",
                     reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda message: message.text == "💡 Советы по выпечке")
def baking_tips_handler(message):
    tips = "\n\n".join(baking_tips)
    bot.send_message(message.chat.id, f"Советы по выпечке:\n\n{tips}")

@bot.message_handler(func=lambda message: message.text == "⏱️ Время приготовления")
def baking_time_info(message):
    time_info = """
    ⏱️ Время приготовления рецептов:

    Яблочный пирог - 40 минут
    Шоколадный кекс - 30 минут
    Овсяное печенье - 15 минут
    Банановый хлеб - 50 минут
    Сырники - 8-10 минут
    Блины - 20-30 минут
    Пирожки с капустой - 20 минут
    Чизкейк - 1 час
        """
    bot.send_message(message.chat.id, time_info)

@bot.message_handler(func=lambda message: message.text == "🆘 Помощь")
def help_handler(message):
    help_text = """
    ℹ️ Помощь по боту:
    - 🔀 Случайный рецепт - бот пришлет случайный рецепт
    - 🔍 Поиск по ингредиентам - поиск рецептов по ингредиенту
    - 📜 Все рецепты - показать все доступные рецепты
    - 💡 Советы по выпечке - полезные советы
    - ⏱️ Время приготовления - информация о времени готовки
    - ❤️ Любимые рецепты - управление вашими любимыми рецептами

    Для возврата в главное меню используйте команду /start
        """
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: message.text == "❤️ Любимые рецепты")
def favorites_menu(message):
    user_id = str(message.from_user.id)
    if user_id not in favorite_recipes or not favorite_recipes[user_id]:
        response = "У вас пока нет любимых рецептов."
    else:
        response = "Ваши любимые рецепты:\n\n" + "\n".join(favorite_recipes[user_id])
    bot.send_message(message.chat.id, response, reply_markup=create_favorites_keyboard(message.from_user.id))

@bot.message_handler(func=lambda message: message.text == "➕ Добавить рецепт в избранное")
def add_favorite_recipe(message):
    msg = bot.send_message(message.chat.id, "Введите название рецепта, который хотите добавить в избранное:",
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, process_add_favorite)

def process_add_favorite(message):
    user_id = str(message.from_user.id)
    recipe_name = message.text
    if recipe_name in recipes:
        if user_id not in favorite_recipes:
            favorite_recipes[user_id] = []
        if recipe_name not in favorite_recipes[user_id]:
            favorite_recipes[user_id].append(recipe_name)
            response = f"Рецепт '{recipe_name}' добавлен в избранное!"
        else:
            response = "Этот рецепт уже в избранном!"
    else:
        response = "Рецепт с таким названием не найден."
    bot.send_message(message.chat.id, response, reply_markup=create_favorites_keyboard(message.from_user.id))

@bot.message_handler(func=lambda message: message.text == "❌ Удалить любимый рецепт")
def remove_favorite_menu(message):
    user_id = str(message.from_user.id)
    if user_id in favorite_recipes and favorite_recipes[user_id]:
        bot.send_message(message.chat.id, "Выберите рецепт для удаления:",
                         reply_markup=create_remove_favorites_keyboard(message.from_user.id))
    else:
        bot.send_message(message.chat.id, "У вас нет любимых рецептов для удаления.",
                         reply_markup=create_favorites_keyboard(message.from_user.id))

@bot.message_handler(func=lambda message: message.text.startswith("❌ ") and len(message.text) > 3)
def remove_favorite_recipe(message):
    user_id = str(message.from_user.id)
    recipe_name = message.text[3:]
    if user_id in favorite_recipes and recipe_name in favorite_recipes[user_id]:
        favorite_recipes[user_id].remove(recipe_name)
        response = f"Рецепт '{recipe_name}' удален из избранного."
    else:
        response = "Этот рецепт не был в избранном."
    bot.send_message(message.chat.id, response, reply_markup=create_favorites_keyboard(message.from_user.id))

@bot.message_handler(func=lambda message: message.text == "🔙 Назад к избранному")
def back_to_favorites(message):
    favorites_menu(message)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад в меню")
def back_to_menu(message):
    bot.send_message(message.chat.id, "Главное меню:", reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda message: message.text in recipes)
def send_recipe(message):
    recipe = message.text
    bot.send_message(message.chat.id, recipes[recipe])

@bot.message_handler(func=lambda message: True)
def send_recipe(message):
    recipe_name = message.text.strip()
    lower_case_recipes = {k.lower(): v for k, v in recipes.items()}
    if recipe_name.lower() in lower_case_recipes:
        bot.send_message(message.chat.id, lower_case_recipes[recipe_name.lower()])
    else:
        bot.send_message(message.chat.id, "Извини, я не знаю такого рецепта. Попробуй другой.")
bot.polling(none_stop=True)