import spacy 
from pathlib import Path
from spacy.matcher import Matcher 
from spacy.attrs import *

def add_event_ent(matcher, doc, i, matches):
    # the match_id will either be FUND or COMPANY
    match_id, start, end = matches[i]
    entity = (match_id, start, end)   
    doc.ents += (entity,)  

def ner(uinput):
    # This is the part where to loads the vocabulary
    ans = ""
    output_dir = './kyzyl'
    nlp = spacy.load(output_dir) 
    # Creating a matcher object
    matcher = Matcher(nlp.vocab) 
    sentence = uinput
    doc = nlp(sentence) 

    patterns = {
            "year": [{'IS_DIGIT': True }], 
            "service": [{"LOWER": "погода"}],
            "time": [{"LOWER": "завтра"}]
          }

    for label, pattern in patterns.items():
        matcher.add(label, add_event_ent, pattern)

    patterns = {
            "time": [{"LOWER": "сегодня"}]
          }

    for label, pattern in patterns.items():
        matcher.add(label, add_event_ent, pattern)

    matches = matcher(doc) 

    for ent in doc.ents:
        ans = ans + ent.label_+" "+ ent.text+"\n"
    return ans

