import telebot
import requests
import server

bot = telebot.TeleBot("5775281001:AAGDsJDcKpwA3asnAsPeu1QzVhiKAojVUik")
ap_key = "ea3ccad46a1b44719978d13cfeb1ad86"
news = []


@bot.message_handler(commands=['start'])
def send_welcome(message):
	login = str(message.from_user.id)
	print(server.reg(login))
	bot.reply_to(message, "Банкок-Таганрог запущен")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	commands ="/start - запуск бота""/start - запуск бота"+"\n"+"/help - список команд"+"\n"+"/news - вызов трех новостей"+"\n"+"/who - бот рассказывает о том кто он"+"\n"
	bot.reply_to(message, commands)
@bot.message_handler(commands=['who'])
def send_welcome(message):
	bot.reply_to(message, "Я как Торонто-Токио, но лучше")

@bot.message_handler(commands=['news'])
def echo_all(message):
	a = requests.get(f'https://newsapi.org/v2/top-headlines?apiKey={ap_key}&country=de&pageSize=3')

	for i in a.json()['articles']:
		news.append([i['title'], i['description'], i['url']])

	print(news)
	answer=""
	for i in range(len(news)):
		# print(i)
		# print(news[i])
		# print(news[i][0],news[i][1],news[i][2])
		# + news[i][1] + "\n"
		answer=news[i][0]+"\n"+ news[i][2]+"\n"
		# print(answer)
		bot.send_message(message.from_user.id, answer)




@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Сам такой")


bot.infinity_polling()
# print('hello')