import telebot

bot = telebot.TeleBot('7915355821:AAHr7vpm3KHZYQEb6Kfg_7OG5YQihT7uBaU')

# обработка новой команды
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Добро пожаловать в мир киберспорта Counter-Strike 2!\nВведите /help для получения всех команд')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Команды бота:\n/top - лучшие игроки по рейтингу 2.1 в 2024 году \n/teams - рейтинг команд на 25.11.2024 \n/spirit - состав команды Team Spirit \n/donk - профиль игрока donk \n/monesy - профиль игрока m0NESY ")
@bot.message_handler(commands=['top'])
def help1(message):
    bot.send_message(message.chat.id,"Лучшие игроки по рейтингу:\n1 - donk (1,35)  \n2 - ZywOo (1,34) \n3 - XANTARES (1,18) \n4 - sh1ro (1,18)")
@bot.message_handler(commands=['teams'])
def teams(message):
    bot.send_message(message.chat.id,"Лучшие команды TOP HLTV:\n 1 - NAVI \n 2 - G2 \n 3 - Vitality \n 4 - Team Spirit \n 5 - MOUZ")
@bot.message_handler(commands=['spirit'])
def spirit(message):
    bot.send_message(message.chat.id,"Состав команды Team Spirit: chopper, sh1ro,magixx,zont1x,donk")
@bot.message_handler(commands=['donk'])
def donk(message):
    bot.send_message(message.chat.id,"Имя: Данил Крышковец \nВозраст: 17 лет \nСтрана: Россия \nКоманда: Team Spirit \nМедалей МВП: 5 \nBetBoom Dacha 2023, IEM Katowice 2024, BLAST Premier Spring Final 2024, BetBoom Dacha Belgrade Season 2")
@bot.message_handler(commands=['monesy'])
def monesy(message):
    bot.send_message(message.chat.id,"Профиль игрока m0NESY: \nИмя: Илья Осипов \nВозраст: 19 лет \nСтрана: Россия \nКоманда: G2 \nМедалей МВП: 4 \nТрофеи: BLAST Premier World Final 2022, IEM Katowice 2023, IEM Cologne 2023, IEM Dallas 2024, BLAST Premier Fall Final 2024, BLAST Premier World Final 2024")
bot.infinity_polling()