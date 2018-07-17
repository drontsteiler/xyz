from __future__ import unicode_literals, print_function
# -*- coding: utf-8 -*-
from spacy.lang.ru import Russian

from pymorphy2 import MorphAnalyzer
from pymorphy2 import units
import string


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

    translator = str.maketrans('', '', string.punctuation)

    uinput = uinput.translate(translator)

    doc = nlp(uinput.lower())



    # test the trained model
    #test_text = 'ты нравятся Берлин?'
    #doc = nlp(test_text)
    text = u""


    for token in doc:
    #print(token, token.lemma, token.lemma_)
    #print(lemmatize_text(token.lemma_))
        text = text + " " + lemmatize_text(token.lemma_)

    doc = nlp(text)

    text = u""
    # load a trained stop words model

    for word in doc:
        if word.is_stop==False:
            text = text + " " + word.lemma_
    return text

