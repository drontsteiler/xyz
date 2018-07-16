from __future__ import unicode_literals, print_function

from spacy.lang.ru import Russian

from pymorphy2 import MorphAnalyzer
from pymorphy2 import units


import spacy

def main(uinput):
    morph = MorphAnalyzer(units = [
    units.DictionaryAnalyzer,
        units.UnknAnalyzer
    ])

    def lemmatize_text(word):
        return morph.parse(word)[0].normal_form

    #lemmas = lemmatizer(u'ducks', u'NOUN')
    #assert lemmas == [u'duck']
    nlp = Russian()

    doc = nlp(uinput)



    # test the trained model
    #test_text = 'ты нравятся Берлин?'
    #doc = nlp(test_text)
    text = ""


    for token in doc:
    #print(token, token.lemma, token.lemma_)
    #print(lemmatize_text(token.lemma_))
        text = text + " " + lemmatize_text(token.lemma_)

    doc = nlp(text)

    text = ""
    # load a trained stop words model

    for word in doc:
        if word.is_stop==False:
            text = text + " " + word.lemma_
    return text
