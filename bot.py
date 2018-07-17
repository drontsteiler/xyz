# -*- coding: utf-8 -*-
import spacy
import config
import telebot
#from main import res

from lemma import main
from ruleBasedNER import ner
from chitchat import chat



bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    user_input = message.text
    ans = ""

    global chatOn

    if user_input==u"Хватит болтать":
        chatOn = False
        ans = u"Как я могу вам помочь?"
        bot.send_message(message.chat.id, ans)
        return #if you remove this, it will recognize services even when the chit chat mode is on
    if user_input==u"Давай поболтаем":
        chatOn = True
        
    if chatOn==True:
        ans = chat(user_input)
    else:
        ans = ner(main(user_input))
    if ans=="":
        ans=u"Не поняла. Повторите ваш запрос пожалуйста"
    bot.send_message(message.chat.id, ans)

if __name__ == '__main__':
    chatOn = False
    bot.polling(none_stop=True)
