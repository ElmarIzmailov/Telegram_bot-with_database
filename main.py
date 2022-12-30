import sqlite3
import telebot

bot = telebot.TeleBot("5808038622:AAECs3mnleoFd-5oO5BIf64svRijY10zsRI")

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Welcome')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'hi':
		bot.send_message(message.chat.id, 'You name add in data base')
		
		us_id = message.from_user.id
		us_name = message.from_user.first_name
		us_sname = message.from_user.last_name
		username = message.from_user.username
		
		db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


bot.polling(none_stop=True)