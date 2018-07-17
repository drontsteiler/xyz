from lemma import main
from ruleBasedNER import ner
from chitchat import chat

def res(user_input):
    chatOn = False

    if user_input=="Хватит болтать":
        chatOn = False
        ans = "Как я могу вам помочь?"
        return ans
    if user_input=="Давай поболтаем":
        chatOn = True

    if chatOn==True:
        ans = chat(user_input)
    else:
        ans = ner(main(user_input))
    
    return ans


