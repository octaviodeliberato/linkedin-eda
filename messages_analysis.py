# IMPORTS ---------------------------------------------------------------------
import pandas as pd 
import numpy as np
import spacy 
from spacy.language import Language

# Usage as a decorator
@Language.component("my_component")
def my_component(doc):
   # Do something to the doc
   return doc

# Usage as a function
Language.component("my_component2", func=my_component)


# DATA ------------------------------------------------------------------------
messages = pd.read_csv('data/messages.csv')
messages.head(10)

# Some tests
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(factory_name='my_component2', name='my_component', last=True)
text = 'This is an english text.'
doc = nlp(text)

# document level language detection.
doc_json = doc.to_json()

# save doc_json to a file
import json
with open('data/doc.json', 'w') as f:
    json.dump(doc_json, f)

# more tests
doc = nlp(messages['CONTENT'][0])
with open('data/doc.json', 'w') as f:
    json.dump(doc.to_json(), f)

# Now, the real deal
from classes.textprocessing import TextProcessing

preprocessor = TextProcessing()

preprocessor.preprocess(messages['CONTENT'][0])

msgs = []
for message in messages['CONTENT']:
    try:
        msgs.append(preprocessor.preprocess(message))
    except:
        msgs.append('Error')

# WORDCLOUD ------------------------------------------------------------------- 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def make_wordcloud(word_count):
    """Function to make a wordcloud from new_text

    Args:
        word_count (dict): dict from string to float, containings words and their
        associated frequency.
    """
    wordcloud = WordCloud(
        width            = 800, 
        height           = 800, 
        min_font_size    = 10,
        background_color = 'black', 
        colormap         = 'Set2', 
        collocations     = False
    ).generate_from_frequencies(word_count)
    
    fig = plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud, interpolation='bilinear') 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.show() 
    
    return fig

from collections import Counter

word_counter = Counter(' '.join(msgs).split())

make_wordcloud(word_counter)
