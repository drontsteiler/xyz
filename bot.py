import spacy
import config
import telebot
from main import res

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    user_input = message.text
    ans = res(user_input)
    
    bot.send_message(message.chat.id, ans)
if __name__ == '__main__':
    bot.polling(none_stop=True)
