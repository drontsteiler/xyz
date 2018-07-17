# -*- coding: utf-8 -*-
from lemma import main
from ruleBasedNER import ner
from chitchat import chat

def res(user_input):
    chatOn = False

    if user_input==u"Хватит болтать":
        chatOn = False
        ans = u"Как я могу вам помочь?"
        return ans
    if user_input==u"Давай поболтаем":
        chatOn = True

    if chatOn==True:
        ans = chat(user_input)
    else:
        ans = ner(main(user_input))
    
    return ans


